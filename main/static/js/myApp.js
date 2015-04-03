var myApp = angular.module('myApp', ['ui.router', 'ngMaterial', 'ngAria', 'ngAnimate']);

myApp.config(function($httpProvider){
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	$httpProvider.defaults.headers.common['X-CSRFToken'] = '{% csrf_value %}';
});

myApp.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('green')
    .accentPalette('light-blue');
});

myApp.controller('testCtrl', ['$scope', function($scope){
	$scope.test = "ugabuga";
}]);

