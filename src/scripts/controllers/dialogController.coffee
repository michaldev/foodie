class Dialog extends Controller
    constructor : ( $scope, $mdDialog ) ->
        $scope.type           = "bug"
        $scope.bugMessage     = ""
        $scope.featureMessage = ""

        $scope.cancel = ->
            $mdDialog.cancel()

        $scope.send = ->
            $mdDialog.cancel()

            switch $scope.type
                when "bug" then console.log "Wysyłanie błędu: #{$scope.bugMessage}"
                when "feature" then console.log "Wysyłanie propozycji: #{$scope.featureMessage}"
