var myApp = angular.module('myApp', ['ui.router', 'ngMaterial', 'ngAria', 'ngAnimate']);

myApp.config(function($httpProvider){
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	$httpProvider.defaults.headers.common['X-CSRFToken'] = '{% csrf_value %}';
});

myApp.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('green')
    .accentPalette('amber');
});

myApp.controller('mainCtrl', ['$scope', '$mdSidenav', function($scope, $mdSidenav){
	$scope.openLeftMenu = function() {
    	$mdSidenav('left').toggle();
    
    	console.log("test");
  	};
}]);

myApp.directive('myDirective', function($compile){
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


			

			
			/*var itemActive = false;
			console.log("dyrek");

			

			iElm.bind('click', function(event){
				console.log("Pokazuj");

				$("body").append($compile('<md-backdrop class="md-backdrop md-default-theme"></md-backdrop><div id="my-dropdown" class="md-select-menu-container my-theme md-default-theme md-active md-clickable">'+
					'<md-select-menu class="md-default-theme">'+
						'<md-content class="md-default-theme my-theme2">'+
							'<md-option md-ink-ripple="#000">'+
								'<div class="md-text">'+
								'asd'+
								'</div>'+
							'</md-option>'+
						'</md-content>'+
					'</md-select-menu>'+
				'</div>')($scope));
				$scope.$apply();

				itemActive = true;
				event.stopPropagation();
			});
			
			
			$(document).click(function(event){
				console.log("Kasuj-klik");
				console.log(itemActive);
				if(itemActive){
					console.log("Kasuj");
					$("#my-dropdown").remove();
					$(".md-backdrop").remove();
					itemActive = false;

					
				}
			}); */
		}	
	};
});

