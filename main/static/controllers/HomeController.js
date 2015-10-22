app.controller('HomeController', ['$scope', '$http', function($scope, $http) {
  $scope.search = [];

  $scope.search.searchItem = function(item) {

    console.log($scope.search.searchText);
    $http.get("/basefood/productsearch?search=" + $scope.search.searchText).success(function(data, status, headers, config) {
      $scope.search.items = data;
      $scope.search.blank = false;
		if(data.length > 0){ 
			 $scope.search.blank = false;
		}
		else {
			$scope.search.blank = true;
		}
    }).error(function(data, status, headers, config) {
      console.log('errorCatB');
    });
  }


}]);
