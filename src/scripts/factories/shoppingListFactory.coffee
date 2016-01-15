class ShopList
    selected : null
    products : []

    addProduct : ( product ) =>
        @products.push product

    selectProduct : ( product ) =>
        @selected = product

    unselectProduct : ->
        @selected = null


angular.module( "app" ).factory "shoppingListFactory", ->
    return new ShopList
