var jaabApp = angular.module('jaab', ['ngRoute']);

jaabApp.config(function($routeProvider, $interpolateProvider) {

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $routeProvider

        .when('/companies', {
            templateUrl : "/templates/companies.html",
            controller  : 'companiesController'
        })

        .when('/companies/:id/employees', {
            templateUrl : "/templates/employees.html",
            controller  : 'employeesController'
        })

        .when('/companies/:company_id/employees/:employee_id/edit', {
            templateUrl : "/templates/employee.html",
            controller  : 'editEmployeeController'
        })

        .when('/companies/:company_id/employees/add', {
            templateUrl : "/templates/employee.html",
            controller  : 'editEmployeeController'
        })
});

jaabApp.controller('companiesController', function($scope, $http) {

    $http.get("/api/v1/company")
        .then(function(response){
            $scope.companies = response.data
            if (response.data.length > 0)
                $scope.company = $scope.companies[0]
        })

    $scope.selectCompany = function(comp){
        $scope.company = comp
    }

})

jaabApp.controller('employeesController',
    function($scope, $http, $routeParams, $location) {

        $scope.companyId = companyId = $routeParams.id

        $http.get("/api/v1/company/"+ companyId)
            .then(function(response){
                $scope.company = response.data
                $scope.employees = response.data.employees
                if ($scope.employees.length > 0)
                    $scope.employee = $scope.employees[0]
            })

        $scope.selectEmployee = function(emp){
            $scope.employee = emp
        }

        $scope.delete_employee = function(employeeId){
            $http.delete("/api/v1/company/"+ $scope.companyId + "/employee/" + employeeId)
            .then(function(){
                $scope.employees.splice(employeeId, 1)
                $scope.employee = $scope.employees[0]
            })
        }
    })

jaabApp.controller('editEmployeeController',
    function($scope, $http, $routeParams, $location) {

        $scope.companyId = $routeParams.company_id;
        $scope.employeeId = $routeParams.employee_id;

        if ($scope.employeeId == undefined){
            $scope.action = "Add"
            $scope.employee = {}
        }
        else{
            $scope.action = "Edit"

            $http.get("/api/v1/company/"+ $scope.companyId + "/employee/" + $scope.employeeId)
            .then(function(response){
                $scope.employee = response.data
            })
        }

        $scope.postEmployee = function(action, employee, companyId, emplyeeId){

            if (action == "Add"){
                url = "/api/v1/company/"+ companyId + "/employee"
            }
            else {
                url = "/api/v1/company/"+ companyId + "/employee/" + emplyeeId
            }

            $http.post(url, employee).then(
                function(){
                    $location.path("/companies/" + companyId + "/employees")
                })
        }

    })
