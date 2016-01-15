configuration   = require "./../configuration"

class ShoppingList extends Controller
    constructor : ( $scope, $mdSidenav, shoppingListFactory ) ->
        $scope.list     = null
        $scope.amount   = null
        $scope.selected = null

        $scope.$watch(
            ( => shoppingListFactory.selected ),
            ( => $scope.selectProduct() )
        )

        $scope.$watch(
            ( => shoppingListFactory.products ),
            ( => $scope.refreshProductList() )
        )

        $scope.$watch(
            ( => $mdSidenav( "right" ).isOpen() ),
            ( => $scope.resetSelectedProduct() )
        )

        $scope.addProduct = =>
            $scope.amount         ?= 1
            $scope.selected.amount = $scope.amount

            shoppingListFactory.addProduct $scope.selected
            shoppingListFactory.unselectProduct()

            $scope.amount   = null
            $scope.selected = null

        # Selects a product and open the right menu
        $scope.selectProduct = =>
            $scope.amount   = 0
            $scope.selected = shoppingListFactory.selected
            $mdSidenav( "right" ).open() if $scope.selected

        # Unselects product and closes the right menu
        $scope.unselectProduct = =>
            $mdSidenav( "right" ).close()
            shoppingListFactory.unselectProduct()

        # Automatically unselect product when menu closes
        $scope.resetSelectedProduct = =>
            $scope.unselectProduct() unless $mdSidenav( "right" ).isOpen()

        $scope.refreshProductList = =>
            $scope.list = shoppingListFactory.products
