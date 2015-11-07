var app = angular.module('MainApp', ['ngMaterial', 'ngAria', 'ngAnimate', 'ui.router']);

app.controller('ToolbarController', ['$scope', '$mdSidenav', function($scope, $mdSidenav){
	$scope.openLeftMenu = function() {
    	$mdSidenav('left').toggle();
  	};

}]);

app.controller('MainController', ['$scope', '$http', function($scope, $http){
	  $scope.password = "";
	  $scope.email = "";
	  $scope.login = function() {
		$http({
			method: 'POST',
			url: '/rest-auth/login/',
			data: "username=root&password=toor",
			headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		}).then(function successCallback(response) {
			$scope.logged = true;
			  }, function errorCallback(response) {
				  console.log("niepowodzenie");
				  console.log(response);
			  });
	  }

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

app.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/home");

  $stateProvider
    .state('home', {
      url: "/home",
      templateUrl: "/views/home",
      controller: 'HomeController'
    })
        	.state('vitamins', {
	        url: '/vitamins/:vitaminSlug-:vitaminID',
	        templateUrl: '/views/vitamins',
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
});

app.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
