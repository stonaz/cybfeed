var cyberFeed = angular.module('cyberFeed', ['cyberFeedServices'])

cyberFeed.controller('cyberFeedController', ['$scope', 'sendData', function ($scope, sendData) {
    console.log('controller created')
    var scope = $scope;
    scope.data = {};
    scope.response = sendData.output();
    scope.$watch(sendData.output,
    function (newValue, oldValue, scope) {
        console.log(newValue.length);
        
        if (newValue && newValue !== oldValue) {
            if (newValue.constructor === Array){
            console.log('array')
            scope.response = scope.test(newValue);
            }
            else {
                scope.response = newValue;
            }
            
        }
    }, true);
    
    //scope.domains = sendData.domains;
    
    scope.test = function(value) {
        l=value.length;
        console.log(l)
        var output = '';
        for (var i=0;i<l;i++){
            console.log(value[i])
            output += value[i]+'\n';
        }
        
        return output;
    }
    
    //scope.setData = function(data) {
    //    console.log('get domains')
    //    scope.domains = data;
    //}
    //     
    //sendData.getXML(scope.setData);
    
        scope.domains = [{
        id: 1,
        name: 'www.example.com'
    }, {
        id: 2,
        name: 'www.example.it'
    }, {
        id: 3,
        name: 'www.example.org'
    }, {
        id: 4,
        name: 'www.example.net'
    }];
   

    scope.callService = function () {
        sendData.list();
    };


    scope.sendDataToSocket = function (name, index) {
        //console.log($scope.data[index])
        var data = {}
        data.name = name;
        data.action = scope.data[index].action;
        sendData.send(data,'/socket/');
    }
    
    scope.updateConfig = function (name, index) {
        //console.log($scope.data[index])
        var data = {}
        data.name = name;
        data.action = scope.data[index].action;
        sendData.send(data,'/socket/update-config/');
    }
}]);

