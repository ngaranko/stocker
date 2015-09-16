var imagesApp = angular.module('imagesApp', []);

imagesApp.controller('ImageListCtrl', function ($scope, $http) {
  $http.get('/api/images').success(function(data) {
    $scope.images = data;
  });

});
