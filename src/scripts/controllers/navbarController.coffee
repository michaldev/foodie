configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"

class Navbar extends Controller
    constructor : ( $scope, $http, $state, changeStateFactory, $mdDialog ) ->
        apiHost = generateApiHost configuration.api

        $scope.vitaminSlug      = undefined
        $scope.vitaminID        = undefined
        $scope.preservativeSlug = undefined
        $scope.preservativeID   = undefined

        $http.get "#{apiHost}/vitamins"
            .success ( data, status, headers, config ) ->
                $scope.vitaminSlug = data[ 0 ].slug
                $scope.vitaminID   = data[ 0 ].id

        $http.get "#{apiHost}/preservatives"
            .success ( data, status, headers, config ) ->
                $scope.preservativeSlug = data[ 0 ].slug
                $scope.preservativeID   = data[ 0 ].id

        $scope.showBugDialog = ( event ) ->
            $mdDialog.show
                controller  : "dialogController"
                templateUrl : "/partials/dialog.html"
                parent      : angular.element document.body
                targetEvent : event
