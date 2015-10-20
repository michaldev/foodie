var app = angular.module('YourApp', ['ngMaterial', 'ngAria', 'ngAnimate', 'ngRoute']);

app.controller('YourController', ['$scope', '$mdSidenav', function($scope, $mdSidenav){
	$scope.openLeftMenu = function() {
    	$mdSidenav('left').toggle();
  	};

}]);

app.config(function($mdThemingProvider) {
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

app.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      controller: 'HomeController',
      templateUrl: 'views/home'
    });
    .otherwise({
      redirectTo: '/'
    });
});