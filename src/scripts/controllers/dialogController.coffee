configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"

class Dialog extends Controller
    constructor : ( $scope, $http, $mdDialog ) ->
        apiHost = generateApiHost configuration.api

        $scope.type         = 0
        $scope.title        = ""
        $scope.mail         = ""
        $scope.description  = ""

        $scope.cancel = ->
            $mdDialog.cancel()

        $scope.send = ->
            request = $http
                method : "PUT"
                url    : "#{apiHost}/contact"
                data   :
                    type        : $scope.type
                    title       : $scope.title
                    mail        : $scope.mail
                    description : $scope.description

            request.then ( -> $mdDialog.cancel() ), # On success
                         ( -> $mdDialog.cancel() )  # On error
