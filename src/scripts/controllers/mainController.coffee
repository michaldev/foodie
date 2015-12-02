configuration   = require "./../configuration"
delay           = require "./../utils/delay"

class Main extends Controller
    constructor : ( $scope, $mdSidenav ) ->
        $scope.openLeftMenu = ->
            $mdSidenav( "left" ).toggle()

        # Loading animation
        if configuration.load
            delay 1500, ->
                $("#loader").animate {
                    width: 0
                    height: 0
                    opacity: 0
                }, 300, ->
                    delay 400,  -> $(".loader").append "<div class='star-anim-circle'></div>"
                    delay 800,  -> $(".star-anim-circle").transition { scale: 100 }
                    delay 1400, -> $(".star-anim-circle").transition { scale: 200 }
                    delay 1900, ->
                        $(".loader").fadeOut "slow"
                        $(".star-anim-circle").transition { scale: $( window ).width() * 1.2 }
        else
            $(".loader").css "display", "none"
