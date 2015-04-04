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

myApp.controller('leftSectionCtrl', ['$scope', '$mdSidenav', function($scope, $mdSidenav){
	var isPosChanged = false;

	$scope.openLeftMenu = function() {
    	$mdSidenav('left').toggle();
    
    	console.log(isPosChanged);
  	};


  	$scope.bazaProduktow = [
		{	
			"Kategoria": "MLECZNE", 
			"Towary":[
						{
							"Id": "1",
							"Nazwa": "Maślanki"
						},
						{
							"Id": "2",
							"Nazwa": "Jogurty"
						}
					]

		},
		{	
			"Kategoria": "INNE", 
			"Towary":[
						{
							"Id": "1",
							"Nazwa": "Costam"
						},
						{
							"Id": "2",
							"Nazwa": "Jakieśtam"
						}
					]

		}
	];
}]);

