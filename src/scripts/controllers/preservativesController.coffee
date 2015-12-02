configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.debug )

class Preservatives extends Controller
    constructor : ( $scope, $stateParams, $http ) ->
        apiHost = generateApiHost configuration.api

        $scope.preservativeID   = $stateParams.preservativeID
        $scope.preservativeSlug = $stateParams.preservativeSlug
        $scope.preservatives    = null
        $scope.functions        = []

        $scope.functions.preservativeChange = ( preservativeSlug, id ) ->
            $scope.preservativeID   = id
            $scope.preservativeSlug = preservativeSlug

        $http.get "#{apiHost}/preservatives"
            .success ( data, status, headers, config ) ->
                $scope.preservatives = data
                debug "[PRESERVATIVES] Preservatives:", data
            .error ( data, status, headers, config ) ->
                debug "[PRESERVATIVES] Preservatives error"
