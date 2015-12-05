angular.module( "app", [
    "ngAria",
    "ngAnimate",
    "ngCookies",
    "ngMessages",
    "ngMaterial",
    "dcbImgFallback",
    "ui.router"
    ] )

.config ( $httpProvider ) ->
    $httpProvider.defaults.xsrfCookieName = "csrftoken"
    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken"

.config ( $mdThemingProvider ) ->
    $mdThemingProvider
        .definePalette "custom-green",
    	    "50"   : "#edf7ee"
    	    "100"  : "#c9e7ca"
    	    "200"  : "#a6d7a8"
    	    "300"  : "#3D9C40"
    	    "400"  : "#6abc6d"
    	    "500"  : "#4caf50"
    	    "600"  : "#439946"
    	    "700"  : "#39833c"
    	    "800"  : "#306d32"
    	    "900"  : "#265828"
    	    "A100" : "#c9e7ca"
    	    "A200" : "#a6d7a8"
    	    "A400" : "#6abc6d"
    	    "A700" : "#39833c"
    	    "contrastDefaultColor" : "light"
        .theme "default"
    	.accentPalette "deep-orange"
    	.primaryPalette "custom-green"

.config ( $stateProvider, $urlRouterProvider ) ->
    $urlRouterProvider.otherwise "/home"

    $stateProvider.state "home",
        url         : "/home"
        templateUrl : "/partials/home.html"
        controller  : "homeController"

    $stateProvider.state "about",
        url         : "/about"
        templateUrl : "partials/about.html"
        controller  : "aboutController"

    $stateProvider.state "product",
        url         : "/product/:productSlug"
        templateUrl : "/partials/product.html"
        controller  : "productController"

    $stateProvider.state "category",
        url         : "/category/:categoryID-:categoryName"
        templateUrl : "/partials/category.html"
        controller  : "categoryController"

    $stateProvider.state "vitamins",
        url         : "/vitamins/:vitaminSlug-:vitaminID"
        templateUrl : "/partials/vitamins.html"
        controller  : "vitaminsController"

    $stateProvider.state "preservatives",
        url         : "/preservatives/:preservativeSlug-:preservativeID"
        templateUrl : "/partials/preservatives.html"
        controller  : "preservativesController"

.run ( $http, $cookies ) ->
    $http.defaults.headers.put[ "X-CSRFToken" ] = $cookies[ "csrftoken" ]

# Load all the components:
require "./bootstrap"