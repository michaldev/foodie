/**
 * jQuery.browser.mobile (http://detectmobilebrowser.com/)
 *
 * jQuery.browser.mobile will be true if the browser is a mobile device
 *
 **/
(function(a){(jQuery.browser=jQuery.browser||{}).mobile=/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))})(navigator.userAgent||navigator.vendor||window.opera);
if(jQuery.browser.mobile)
{
   $("#main-toolbar").attr("md-scroll-shrink", "true");
}
else
{
   console.log('You are not using a mobile device!');
   
}



var myApp = angular.module('myApp', ['ngCookies', 'ui.router', 'ngMaterial', 'ngAria', 'ngAnimate', 'lumx']);






myApp.config(function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
myApp.config(function($mdThemingProvider) {
	$mdThemingProvider.definePalette('customGreen', {
    "50": "#edf7ee",
    "100": "#c9e7ca",
    "200": "#a6d7a8",
    "300": "#3D9C40",
    "400": "#6abc6d",
    "500": "#4caf50",
    "600": "#439946",
    "700": "#39833c",
    "800": "#306d32",
    "900": "#265828",
    "A100": "#c9e7ca",
    "A200": "#a6d7a8",
    "A400": "#6abc6d",
    "A700": "#39833c",
    'contrastDefaultColor': 'light',    // whether, by default, text (contrast)
                                        // on this palette should be dark or light
    'contrastDarkColors': ['50', '100', //hues which contrast should be 'dark' by default
     '200', '300', '400', 'A100'],
    'contrastLightColors': undefined    // could also specify this if default was 'dark'
});
  $mdThemingProvider.theme('default')
    .primaryPalette('customGreen')
    .accentPalette('deep-orange');
});

myApp.run(function($http, $cookies) {
    $http.defaults.headers.put['X-CSRFToken'] = $cookies['csrftoken'];
});

myApp.config(function($stateProvider, $urlRouterProvider) {
    
    $urlRouterProvider.otherwise('/home');
    
    $stateProvider
        
        // HOME STATES AND NESTED VIEWS ========================================
        .state('home', {
	        url: '/home',
	        templateUrl: 'homeview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http, $cookies) {
	        	$scope.searchCtrl = [];
	        	
	        	$scope.searchCtrl.searchItem = function(item){
	        		console.log($scope.searchCtrl.searchText);
	        		$scope.searchCtrl.isClicked = true;

		        		$http.get("/basefood/productsearch?search=" + $scope.searchCtrl.searchText).success(function(data, status, headers, config) {
			    		console.log('successCat');

			    		$scope.searchCtrl.itemsToShow = data;

			    		console.log("After search: " + data);
			    		


					}).error(function(data, status, headers, config) {
				    	console.log('errorCatB');
					});
	        	}
	        	
	           
			}
    	})
        .state('about', {
	        url: '/about',
	        templateUrl: 'aboutview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http, $cookies) {
	           
			}
    	})
    	.state('productDetail', {
	        url: '/product/:productSlug',
	        templateUrl: 'productview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http) {
	            $scope.slug = $stateParams.productSlug;
	            console.log($scope.slug);

	            $http.get("/basefood/products?slug=" + $scope.slug).success(function(data, status, headers, config) {
		    		console.log('successCatProduct');

		    		$scope.product = data[0];

		    		console.log("Product: ");
		    		console.log(data[0]);

				}).error(function(data, status, headers, config) {
			    	console.log('errorCatB');
				});
			}
    	})
    	.state('vitamins', {
	        url: '/vitamins/:vitaminSlug-:vitaminID',
	        templateUrl: 'vitaminview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http, $state) {
	            
	            $scope.vitaminSlug = $stateParams.vitaminSlug;
	            $scope.vitaminID = $stateParams.vitaminID;


	            
	           

	            $scope.functions = [];

				


	            $scope.functions.vitamineChange = function(vitaminSlug, vitaminID){

	            	console.log("vitaminSlug: " + $scope.vitaminSlug);

	            	//$("#vitamine-" + $scope.vitaminID).css( "background-color", "red" );
	            	$scope.vitaminSlug = vitaminSlug;
	            	$scope.vitaminID = vitaminID;
	            	//$("#vitamine-" + $scope.vitaminID).css( "background-color", "red" );
	            	//console.log($scope.vitaminID);

	            }


	            $http.get("/basefood/vitamins").success(function(data, status, headers, config) {
		    		//console.log('successCatA');

		    		$scope.vitamins = data;

		    		console.log(data);

				}).error(function(data, status, headers, config) {
			    	//console.log('errorCatC');
				});




			}
    	})
    	.state('preservatives', {
	        url: '/preservatives/:preservativeSlug-:preservativeID',
	        onEnter: function() { console.log("enter tab2"); },
	        templateUrl: 'preservativeview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http) {
	            $scope.preservativeID = $stateParams.preservativeID;
	            $scope.preservativeSlug = $stateParams.preservativeSlug;

	            $scope.functions = [];


	            $scope.functions.preservativeChange = function(preservativeSlug, id){
	            	$scope.preservativeID = id;
	            	$scope.preservativeSlug = preservativeSlug;
	            	//console.log($scope.preservativeID);
	            }


	            $http.get("/basefood/preservatives").success(function(data, status, headers, config) {
		    		console.log('successCatC');

		    		$scope.preservatives = data;

		    		console.log(data);

				}).error(function(data, status, headers, config) {
			    	console.log('errorCatC');
				});
			}
    	});
        
        
});

myApp.factory('animationFactory', function(){
	var animationFactory = [];

	animationFactory.firstAnim = true;

	animationFactory.setFirstAnim = function(){
		animationFactory.firstAnim = false;
	}

	animationFactory.getFirstAnim = function(){
		return animationFactory.firstAnim;
	}

	return animationFactory;
});



myApp.controller('mainCtrl', ['$scope', '$mdSidenav', 'animationFactory', function($scope, $mdSidenav, animationFactory){
	$scope.openLeftMenu = function() {
    	$mdSidenav('left').toggle();
  	};



  	$(window).load(function() {
		//$(".loader").delay(5000).append('<div class="star-anim-circle">OK</div>').fadeOut("slow");



	});




  	$(document).ready(function() {
  		setTimeout(function() {		 
			$('#loadingItem').transition({ scale: 0 });
				
				setTimeout(function() {		
					$(".loader").append('<div class="star-anim-circle"></div>');
						setTimeout(function() {		
							$(".star-anim-circle").transition({ scale: 100 });
								setTimeout(function() {		
									$(".star-anim-circle").transition({ scale: 200 });
										setTimeout(function() {		
											$(".star-anim-circle").transition({ scale: $( window ).width()*1.2 });
											$(".loader").fadeOut("slow");


										}, 500);


								}, 600);


						}, 400);
				},400);






		  	


		}, 3000);
	});


}]);

myApp.controller('viewCtrl', ['$scope','animationFactory', function($scope, animationFactory){
		

		$scope.$on('$stateChangeSuccess', function (event, toState) {

			var viewHeight = $("#my-main-container").height();
			var windowHeight = $("body").height();
			var diffHeight = windowHeight - viewHeight;
			console.log("h: " + viewHeight);
			console.log("h: " + windowHeight);
			console.log("h: " + diffHeight);

			$scope.isRunFirstAnim = animationFactory.getFirstAnim();
			console.log("Anim: " + $scope.isRunFirstAnim);

			if($scope.isRunFirstAnim == false){
				$('body').append( $('<div id="my-viewchange-screen" style="position: absolute;top:' + diffHeight + 'px; left:0px; right:100%; height:' + viewHeight + 'px; background-color: #4CAF50; z-index:1001;"></div>') );
			   
				   $( "#my-main-container" ).css({
					    opacity: "0"
					});


				    $("#my-viewchange-screen").delay(0).animate({
						right: '0'
						}, 200, 'easeOutCubic', function() {


							
							$("#my-main-container").delay(200).animate({
								opacity: '1'
								}, 500, 'easeOutCubic', function() {
								console.log("anim2");
							});


							$("#my-viewchange-screen").delay(200).animate({
								right: '100%'
								}, 500, 'easeOutCubic', function() {
								$("#my-viewchange-screen").remove();
							});
				    		
					});
				
			}
	        console.log("tseeses");
	    });
	
}]);

myApp.controller('sidenavCtrl', ['$scope','$http', function($scope, $http){
	
	//http://127.0.0.1:8000/basefood/category
	//http://127.0.0.1:8000/basefood/catmain

	$http.get("/basefood/category").success(function(data, status, headers, config) {
    	console.log('successCat');

    	$scope.categories = data;



		}).error(function(data, status, headers, config) {
	    	console.log('errorCatA');
		});

		
	

}]);

myApp.directive('ngEnter', function() {
        return function(scope, element, attrs) {
            element.bind("keydown keypress", function(event) {
                if(event.which === 13) {
                        scope.$apply(function(){
                                scope.$eval(attrs.ngEnter);
                        });
                        
                        event.preventDefault();
                }
            });
        };
});



myApp.directive('myTooltip',['$compile', function($compile){
	// Runs during compile
	return {
		// name: '',
		// priority: 1,
		// terminal: true,
		// scope: {}, // {} = isolate, true = child, false/undefined = no change
		// controller: function($scope, $element, $attrs, $transclude) {},
		// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
		// restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
		// template: '',
		// templateUrl: '',
		// replace: true,
		// transclude: true,
		// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
		link: function($scope, iElm, iAttrs, controller) {

			var scope = angular.element('md-content').scope();

			//var top = $("#Konserwanty").position().top;
			var top = $("md-content").scrollTop() + $("#Konserwanty").position().top;
			var left = $("#Konserwanty").offset().left + $("#Konserwanty").width() + 46;

			iElm.bind('click', function(){

				

				
				jQuery(('md-content')).append(
				    $compile(  
				        '<div class="my-tooltip md-whiteframe-z2" style="top:'+Math.round(top)+'px; left:'+Math.round(left)+'px;">asdadasd</div>'
				    )(scope)
				);
				$(".my-tooltip").animate({
				    width: "300px",
				    height: "300px",
				    opacity: "1"
				  }, 500, 'easeOutQuad', function() {

				  });
				console.log($("md-content").scrollTop());
			});  
				
		
		}
	};
}]);