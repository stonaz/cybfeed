var cyberFeed = angular.module('cyberFeed', ['cyberFeedServices'])

cyberFeed.controller('cyberFeedController', ['$scope', 'sendData', function ($scope, sendData) {
    console.log('controller created')
    var scope = $scope;
    scope.data = {};
    scope.response = sendData.output();
    scope.$watch(sendData.output,

    function (newValue, oldValue, scope) {
        console.log(newValue);
        if (newValue && newValue !== oldValue) {
            $scope.response = newValue;
        }
    }, true);
    
    //scope.domains = sendData.domains;
    
    scope.setData = function(data) {
        console.log(data)
        scope.domains = data;
    }
         
    sendData.getXML(scope.setData);
   

    scope.callService = function () {
        sendData.list();
    };


    scope.sendDataToSocket = function (name, index) {
        //console.log($scope.data[index])
        var data = {}
        data.name = name;
        data.action = scope.data[index].action;
        sendData.send(data);


        //var json_response=function(){
        //    return sendData.send(data);}
        //console.log('response: ' +json_response())
        //'test';
        //$http.post('/socket/', data).
        //success(function (data, status, headers, config) {
        //    $scope.response = data;
        //    console.log(data)
        //    data_json = JSON.parse(data);
        //    console.log(data_json)
        //    $scope.response = data_json;
        //}).
        //error(function (data, status, headers, config) {
        //    $scope.response = data;
        //
        //    // called asynchronously if an error occurs
        //    // or server returns response with an error status.
        //});

        //$http.post('socket/', data)
        ////.then(fetchTodos)
        //.then(function(response) {
        //    $scope.response=response.data;
        //    console.log(response.data)
        ////$scope.newTodo = {};
        //}),
        //function(error){console.log('error')};
    }
}]);

//cyberFeed.factory('sendData', ['$http',
//
//function ($http) {
//    var message = ''
//    return {
//        output: function () {
//            return (message)
//        },
//        send: function (json) {
//            $http.post('/socket/', json).
//            success(function (data, status, headers, config) {
//                console.log(data)
//                message = data;
//            }).
//            error(function (data, status, headers, config) {
//                console.log(data)
//                message = data.Error;
//            });
//        }
//    };
//}])
//    .config(['$httpProvider', function ($httpProvider) {
//    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
//}]);