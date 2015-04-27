$(document).ready(function() {
    $('body').append( $('<div id="my-greeting-screen" style="position: absolute;top:0;left:0; width:100%; height:100%; background-color: #4CAF50; z-index:1001;"></div>') );
    $("#my-greeting-screen").delay(600).animate({
				    height: "0px",
				  }, 1000, 'easeOutCubic', function() {

				  });
    console.log("test");
});


var myApp = angular.module('myApp', ['ui.router', 'ngMaterial', 'ngAria', 'ngAnimate','ngTouch', 'lumx']);

myApp.config(function($httpProvider){
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	$httpProvider.defaults.headers.common['X-CSRFToken'] = '{% csrf_value %}';
});
myApp.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('green')
    .accentPalette('deep-orange');
});

myApp.config(function($stateProvider, $urlRouterProvider) {
    
    //$urlRouterProvider.otherwise('/home');
    
    $stateProvider
        
        // HOME STATES AND NESTED VIEWS ========================================
        .state('productDetail', {
	        url: '/product/:productID',
	        templateUrl: 'productview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http) {
	            $scope.id = $stateParams.productID;
	            console.log($scope.id);

	            $http.get("/basefood/" + $scope.id).success(function(data, status, headers, config) {
		    		console.log('successCat');

		    		$scope.product = data;

		    		console.log(data);

				}).error(function(data, status, headers, config) {
			    	console.log('errorCatB');
				});
			}
    	})
    	.state('vitamins', {
	        url: '/vitamins/:vitaminID',
	        templateUrl: 'vitaminview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http) {
	            $scope.vitaminID = $stateParams.vitaminID;

	            $scope.functions = [];

	            $scope.functions.vitamineChange = function(id){
	            	$scope.vitaminID = id;
	            	console.log($scope.vitaminID);
	            }


	            $http.get("/basefood/vitamins").success(function(data, status, headers, config) {
		    		console.log('successCatA');

		    		$scope.vitamins = data;

		    		console.log(data);

				}).error(function(data, status, headers, config) {
			    	console.log('errorCatC');
				});




			}
    	})
    	.state('preservatives', {
	        url: '/preservatives/:preservativeID',
	        templateUrl: 'preservativeview',
	        //template: 'test',
	        controller: function($scope, $stateParams, $http) {
	            $scope.preservativeID = $stateParams.preservativeID;

	            $scope.functions = [];


	            $scope.functions.preservativeChange = function(id){
	            	$scope.preservativeID = id;
	            	console.log($scope.preservativeID);
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

myApp.controller('mainCtrl', ['$scope', '$mdSidenav', function($scope, $mdSidenav){
	$scope.openLeftMenu = function() {
    	$mdSidenav('left').toggle();
  	};
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
