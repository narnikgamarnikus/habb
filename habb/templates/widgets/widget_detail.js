{% load token %}
(function() {

// Localize jQuery variable
var jQuery;

/******** Load jQuery if not present *********/
if (window.jQuery === undefined || window.jQuery.fn.jquery !== '3.2.1') {
    var script_tag = document.createElement('script');
    script_tag.setAttribute("type","text/javascript");
    script_tag.setAttribute("src",
        "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js");
  
    if (script_tag.readyState) {
      script_tag.onreadystatechange = function () { // For old versions of IE
          if (this.readyState == 'complete' || this.readyState == 'loaded') {
              alert('scriptLoadHandler');
              scriptLoadHandler();
          }
      };
    } else { // Other browsers
      script_tag.onload = scriptLoadHandler;
    }
    // Try to find the head, otherwise default to the documentElement

} else {
    // The jQuery version on the window is the one we want to use
    jQuery = window.jQuery;
    main();
}

/******** Called once jQuery has loaded ******/
function scriptLoadHandler() {
    // Restore $ and window.jQuery to their previous values and store the
    // new jQuery in our local jQuery variable
    jQuery = window.jQuery.noConflict(true);




    // Call our main function
    surpriseClicked = localStorage.getItem("surpriseClicked");
    if (surpriseClicked == null || surpriseClicked == "null") {
          main();
        }
 
}


/******** Our main function ********/
function main() {

    alert('123123');
    
    var stepform_srcipt = document.createElement('script');
    stepform_srcipt.setAttribute("type", "text/javascript");
    stepform_srcipt.setAttribute("id", "script");
    stepform_srcipt.setAttribute("src", "https://stagingserver.xyz/static/js/stepform.js");
    
    (document.getElementsByTagName("head")[0] || document.documentElement).append(stepform_srcipt);

    jQuery(document).ready(function($) {
        


      alert('312');



    });
}

})(); // We call our anonymous function immediately


