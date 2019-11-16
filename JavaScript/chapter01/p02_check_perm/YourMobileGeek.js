/* Given two strings, write a method to decide 
if one is permutation of the other */

var checkPerm = function(stringOne,  stringTwo) {
    //if different lengths, return false
    if (stringOne.length !==  stringTwo.length ) {
        return false; 
    } 
    //else sort & compare
    else {
        var sortStringOne = stringOne.split('').sort('').join('');
        var sortStringTwo = stringTwo.split('').sort('').join('');
        return sortStringOne === sortStringTwo;
    }
};
