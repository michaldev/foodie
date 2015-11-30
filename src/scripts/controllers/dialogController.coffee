class Dialog extends Controller
    constructor : ( $scope, $http, $mdDialog ) ->
        $scope.type         = 0
        $scope.title        = ""
        $scope.mail        = ""
        $scope.description  = ""

        $scope.cancel = ->
            $mdDialog.cancel()

        $scope.send = ->
            request = $http
                method : "PUT"
                url    : "http://127.0.0.1:8000/basefood/contact"
                data   :
                    type        : $scope.type
                    title       : $scope.title
                    mail        : $scope.mail
                    description : $scope.description

            request.then ( -> $mdDialog.cancel() ), # On success
                         ( -> $mdDialog.cancel() )  # On error
