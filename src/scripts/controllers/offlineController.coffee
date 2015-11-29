class Offline extends Controller
    constructor : ( $scope ) ->
        # Show offline message if there is no internet connection
        $( "#offline-message" ).css( "display", "block" ) if not navigator.onLine

        $scope.close = ->
            $( "#offline-message" ).slideUp()
