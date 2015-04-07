var cyberFeedServices = angular.module('cyberFeedServices', []);

cyberFeedServices.factory('sendData', ['$http',

function ($http) {
    var message = ''
    var domains = []
            
            var url = 'http://localhost:8000/static/data/domains.xml'
            $http.get(url).
            success(function (data, status, headers, config) {
                //console.log(data)
                var x2js = new X2JS();
                var json = x2js.xml_str2json( data );
                console.log(json);
                domains = json;
            }).
            error(function (data, status, headers, config) {
                console.log(status)
                //message = data.Error;
            });
           // return domains;
                
    var domains = [{
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
    return {
        output: function () {
            return (message)
        },
        send: function (json) {
            $http.post('/socket/', json).
            success(function (data, status, headers, config) {
                console.log(data)
                message = data;
            }).
            error(function (data, status, headers, config) {
                console.log(data)
                message = data.Error;
            });
        },
        getXML: function (callback) {
            var url = 'http://localhost:8000/static/data/domains.xml'
            $http.get(url,
                    {transformResponse:function(data) {
                      // convert the data to JSON and provide
                      // it to the success function below
                        var x2js = new X2JS();
                        var json = x2js.xml_str2json( data );
                        return json;
                        }
                    }).
            success(function (data, status, headers, config) {
                callback(data)
                //var x2js = new X2JS();
                //var json = x2js.xml_str2json( data );
                //console.log(json);
                //return json;
            }).
            error(function (data, status, headers, config) {
                console.log(status)
                //message = data.Error;
            });
            return domains;
        },        
        

    };
}])
    .config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);