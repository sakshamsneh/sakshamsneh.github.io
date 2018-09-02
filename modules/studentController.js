mainApp.controller("studentController", function($scope) {
    $scope.student = {
       firstName: "Saksham",
       lastName: "Sneh",
       fees:500,
       
       subjects:[
          {name:'CS1',marks:100},
          {name:'CS2',marks:90},
          {name:'CS3',marks:80}
       ],
       
       fullName: function() {
          var studentObject;
          studentObject = $scope.student;
          return studentObject.firstName + " " + studentObject.lastName;
       }
    };
 });
