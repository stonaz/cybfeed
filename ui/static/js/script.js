angular.module('testApp', [])
.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}])
.controller('AppController', ['$http',function($http) {
    console.log('controller created')
var self = this;
self.data={};
self.response='No response yet';
self.domains = [
{id: 1, name: 'www.example.com'},
{id: 2, name: 'www.example.it'},
{id: 3, name: 'www.example.org'},
{id: 4, name: 'www.example.net'}
];

self.sendDataToSocket = function(name,index) {
    console.log(self.data[index])
var data = {}
data.name=name;
data.action=self.data[index].action;
$http.post('socket/', data)
//.then(fetchTodos)
.then(function(response) {
    self.response=response.data;
    console.log(response.data)
//self.newTodo = {};
}),
function(error){console.log('error')};
}
}]);