configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
generateWebHost = require "./../utils/generateWebHost"

class Navbar extends Controller
    constructor : ( $scope, $http, $state, $mdDialog ) ->
        apiHost = generateApiHost configuration.api
        webHost = generateWebHost configuration.web.path

        $scope.vitaminSlug      = undefined
        $scope.vitaminID        = undefined
        $scope.preservativeSlug = undefined
        $scope.preservativeID   = undefined

        $http.get "#{apiHost}/vitamins"
            .success ( data, status, headers, config ) ->
                $scope.vitaminSlug = data[ 0 ].slug
                $scope.vitaminID   = 0

        $http.get "#{apiHost}/preservatives"
            .success ( data, status, headers, config ) ->
                $scope.preservativeSlug = data[ 0 ].slug
                $scope.preservativeID   = 0

        $scope.showBugDialog = ( event ) ->
            $mdDialog.show
                controller  : "dialogController"
                templateUrl : "#{webHost}/partials/dialog.html"
                parent      : angular.element document.body
                targetEvent : event
