class Dialog extends Controller
    constructor: ( $scope, $mdDialog ) ->
        $scope.cancel = ->
            $mdDialog.cancel()
