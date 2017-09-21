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
              scriptLoadHandler();
          }
      };
    } else { // Other browsers
      script_tag.onload = scriptLoadHandler;
    }
    // Try to find the head, otherwise default to the documentElement
    (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);
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
    jQuery(document).ready(function($) {
        localStorage.removeItem("surpriseClicked");


        var popup_styles = document.createElement('link');
        popup_styles.setAttribute("rel", "stylesheet");
        popup_styles.setAttribute("href", "https://stagingserver.xyz/static/css/popup.css");

        (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(popup_styles);

        jQuery.fn.shake = function (interval, distance, times) {
            interval = typeof interval == "undefined" ? 100 : interval;
            distance = typeof distance == "undefined" ? 10 : distance;
            times = typeof times == "undefined" ? 3 : times;
            var jTarget = $(this);
            jTarget.css('position', 'relative');
            for (var iter = 0; iter < (times + 1) ; iter++) {
                jTarget.animate({ top: ((iter % 2 == 0 ? distance * Math.random() : distance * Math.random() * -1)), left: ((iter % 2 == 0 ? distance * Math.random() : distance * Math.random() * -1)) }, interval);
            }
            return jTarget.animate({ top: 0 , left: 0 }, interval);
        }

        jQuery.fn.setSurpriseClicked = function(){
          localStorage.setItem("surpriseClicked", "true");
        };

        jQuery('#surpriseButton').click(function() {
          setSurpriseClicked();
        });

        // We can use jQuery 1.4.2 here
        jQuery('body').append(
          '<a href="#popup1" id="surpriseButton">' +
          '<div style="position: fixed; top: 12.5em; right: 0;">' +
          '<img style="width: 5em; height: 5em" id="surprise" src="https://it.utah.edu/_images/taylor/gift.png">' +
          '</div>' +
          '</a>'
          )
        jQuery('body').append(
          '<div id="popup1" class="overlay">' +
          '<div class="popup">' +
          '<h2>Here i am</h2>' +
          '<a class="close" href="#">&times;</a>' +
          '<div class="content">Thank to pop me out of that button, but now im done so you can close this window.</div>' +
          '</div>' +
          '</div>'
          )
        surprise = jQuery('#surprise');
        surprise.shake(100,2.5,300);

        alert('ready');
        console.log('fuck that shit!')
    });
}

})(); // We call our anonymous function immediately


