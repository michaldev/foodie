configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.debug )

class Vitamins extends Controller
    constructor : ( $scope, $stateParams, $http, $state ) ->
        apiHost = generateApiHost configuration.api

        $scope.vitaminSlug  = $stateParams.vitaminSlug
        $scope.vitaminID    = $stateParams.vitaminID
        $scope.vitamins     = null
        $scope.functions    = []

        $scope.functions.vitamineChange = ( vitaminSlug, vitaminID ) ->
            debug "[VITAMINS] Vitamin:", $scope.vitaminSlug

            $scope.vitaminSlug  = vitaminSlug
            $scope.vitaminID    = vitaminID

        $http.get "#{apiHost}/vitamins"
            .success ( data, status, headers, config ) ->
                $scope.vitamins = data
                debug "[VITAMINS] Vitamins:", data
            .error ( data, status, headers, config ) ->
                debug "[VITAMINS] Vitamins error"
