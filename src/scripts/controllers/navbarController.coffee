class Navbar extends Controller
    constructor: ( $scope, $state, changeStateFactory, $mdDialog ) ->
        $scope.showBugDialog = ( event ) ->
            $mdDialog.show
                controller  : "dialogController"
                templateUrl : "/partials/dialog.html"
                parent      : angular.element document.body
                targetEvent : event
