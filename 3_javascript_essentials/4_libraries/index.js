// jQuery syntax
// Thr syntax is tailored for selecting HTML elements and then performing actions on those elements

// $(selector).action()
// EG
// $(this).hide()
// $("p").hide()
// $(".test").hide()
// $("#test").hide()

// jQuery has a function ready() that is designed to take cre of that  , in that it waits for the page to be ready (all HTML elements ready)

// Essentially you would just place the code inside the ready function

// javascript
function myFunction() {
   let obj = document.getElementById("h01")
   obj.innerHTML = "Hello JQuery"
}

// jQuery
function myFunctionjQ() {
   $("#h01").html("Hello JQuery")
}

$(document).ready(function () {
	myFunctionjQ()
});