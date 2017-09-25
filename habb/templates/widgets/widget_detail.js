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
    
    var bootstrap_script = document.createElement('script');
    bootstrap_script.setAttribute("type", "text/javascript");
    bootstrap_script.setAttribute("integrity", "sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1");
    bootstrap_script.setAttribute("crossorigin", "anonymous");
    bootstrap_script.setAttribute("src", 
      "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js")
    
    /*
    var popper_script = document.createElement('script');
    popper_script.setAttribute("type", "text/javascript");
    popper_script.setAttribute("integrity", "sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4");
    popper_script.setAttribute("crossorigin", "anonymous");
    popper_script.setAttribute("src", 
      "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js")
    var bootstrapmd_script = document.createElement('script');
    bootstrapmd_script.setAttribute("type", "text/javascript")
    bootstrapmd_script.setAttribute("src", 
      "https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.3.2/js/mdb.min.js")
    */
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


    var stepform_srcipt = document.createElement('script');
    stepform_srcipt.setAttribute("type", "text/javascript");
    stepform_srcipt.setAttribute("src", "https://stagingserver.xyz/static/js/stepform.js");


    (document.getElementsByTagName("head")[0] || document.documentElement).append(stepform_srcipt);
    (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);

    //(document.getElementsByTagName("head")[0] || document.documentElement).append(bootstrap_script);

    //(document.getElementsByTagName("head")[0] || document.documentElement).appendChild(popper_script);
    //(document.getElementsByTagName("head")[0] || document.documentElement).appendChild(bootstrap_script);
    //(document.getElementsByTagName("head")[0] || document.documentElement).appendChild(bootstrapmd_script);


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
        
        var stepform_styles = document.createElement('link');
        stepform_styles.setAttribute("rel", "stylesheet");
        stepform_styles.setAttribute("href", "https://stagingserver.xyz/static/css/stepform.css");

        //var bootstrap_styles = document.createElement('link');
        //bootstrap_styles.setAttribute("rel", "stylesheet");
        //bootstrap_styles.setAttribute("href", "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css");
        //bootstrap_styles.setAttribute("integrity", "sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M");
        //bootstrap_styles.setAttribute("crossorigin","anonymous"); 

        //var bootstrapmd_styles = document.createElement('link');
        //bootstrapmd_styles.setAttribute("rel", "stylesheet");
        //bootstrapmd_styles.setAttribute("href", "https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.3.2/css/mdb.min.css");

        (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(popup_styles);
        (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(stepform_styles);

        //(document.getElementsByTagName("head")[0] || document.documentElement).appendChild(bootstrap_styles);
        //(document.getElementsByTagName("head")[0] || document.documentElement).appendChild(bootstrapmd_styles);

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
          '<a id="surprise_button" href="#popup1">' +
          '<div style="position: fixed; top: 45%; right: 0;">' +
          '<img style="width: 5em; height: 5em" id="surprise" src="https://it.utah.edu/_images/taylor/gift.png">' +
          '</div>' +
          '</a>'
          )

        jQuery('body').append('<div class="modal fade" id="exampleModalLong" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true"> <div class="modal-dialog" role="document"> <div class="modal-content"> <div class="modal-header"> <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5> <button type="button" class="close" data-dismiss="modal" aria-label="Close"> <span aria-hidden="true">&times;</span> </button> </div><div class="modal-body"> ... </div><div class="modal-footer"> <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> <button type="button" class="btn btn-primary">Save changes</button> </div></div></div></div>')
        
        jQuery('body').append(
          '<div id="popup1" class="overlay">' +
          '<div class="popup">' +
          '<h2>Here i am</h2>' +
          '<a class="close" id="close" href="#">&times;</a>' +
          '<form class="stepform" action="" method="post"><!--fieldset class="sf-step"><legend>1. Basic Details</legend><p><label class="control-label" for="firstname">First Name</label><input class="form-control" id="firstname" name="firstname" data-validate="1"/></p><p><label class="control-label" for="lastname">Last Name</label><input class="form-control" id="lastname" name="lastname" data-validate="1"/></p></fieldset--><fieldset class="sf-step"><legend>1. Как вас зовут?</legend> <p><label class="control-label" for="name">Имя</label><input class="form-control" id="name" name="mobile" data-validate="2"/></p></fieldset><fieldset class="sf-step"> <legend>2. Как с вами связаться?</legend> <p><label class="control-label" for="mobile">Номер телефона</label><input class="form-control" type="tel" id="mobile" name="mobile" data-validate="10"/></p><p><label class="control-label" for="email">Электронная почта</label><input class="form-control" id="email" name="email" data-validate="email"/></p></fieldset><fieldset class="sf-step"><legend>3. Расскажите друзьям</legend><p><a id="vk_share_button">SHARE</a></p></fieldset></form>' +
          '<div class="content">Thank to pop me out of that button, but now im done so you can close this window.</div>' +
          '<button id="ab">Click</button>' +
          '</div>' +
          '</div>'
          )
        

        //jQuery('body').append('<div class="modal fade" id="centralModalSuccess" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog modal-notify{% if widget.form_type is 'color_form' %}{{widgte.color_form_color}}{% endif %}" role="document"> <div class="modal-content">{% if widget.form_type is 'color_form' %}<div class="modal-header"> <p class="heading lead">{{widget.title}}</p><button type="button" class="close" data-dismiss="modal" aria-label="Close"> <span aria-hidden="true" class="white-text">&times;</span> </button> </div>{% endif %}<div class="modal-body">{% if widget.form_type is 'color_form' %}<div class="text-center"> <i class="{{widget.color_form_icon}}{{widget.color_form_icon_size}}mb-3{{widget.color_form_animated}}"></i> <p>{{widget.offer}}</p></div>{% elif widget.form_type is 'person_form' %}<div class="row"> <div class="col-3 text-center">{#% avatar widget.user class="img-fluid z-depth-1-half rounded-circle" alt="user.full_name" id="user_avatar" %#}<div style="height: 10px"></div><p class="title mb-0">{{widget.user.full_name}}</p><p class="text-muted " style="font-size: 13px">{{widget.user.profession}}</p></div><div class="col-9"> <p><strong>{{widget.offer}}</strong></p><p>{{widget.text}}</p></div></div>{% elif widget.form_type is 'image_form' %}<div class="card card-image" style="background-image: url('{{widget.image}}'); width: 28rem;"> <div class="text-white rgba-stylish-strong py-5 px-5 z-depth-4"> </div></div>{% endif %}</div>{% if widget.form_type is not 'image_form' %}<div class="modal-footer justify-content-center"> <a type="button" class="btn btn-primary-modal">{{button.text}}<i class="{{button.icon}}{{button.icon_size}}mb-3"></i></a> <a type="button" class="btn btn-outline-secondary-modal waves-effect" data-dismiss="modal">{{button_cancel.text}}</a> </div>{% endif %}</div></div></div>');
        surprise = jQuery('#surprise');
        surprise.shake(100,2.5,300);
        

        var leed_data = JSON.stringify({
          "widget": "{{ object.pk }}",
          "email": "test@test.com",
          "phone_number": "+375259075055",
          "first_name": "Test",
          "last_name": "Test"
        });

        var widget_opened_data = JSON.stringify({
          "opened": "{{ opened }}",
        });

        var widget_closed_data = JSON.stringify({
          "closed": "{{ closed }}",
        });

        jQuery('#ab').click(function () {
            $.ajax({
                type: "POST",
                data: leed_data,
                url: "https://stagingserver.xyz/api/leeds/?token={{ user_token }}",
                cache: false,
                dataType: "json",
                contentType : 'application/json',
                processData: false,
                success: function (json) { 
                  console.log(json);
                },
                error: function (error) { 
                  console.log(error);
                }
            });
        });

        jQuery('#surprise_button').click(function () {
            $.ajax({
                type: "PUT",
                data: widget_opened_data,
                url: "https://stagingserver.xyz/api/widgets/{{ object.pk }}/?token={{ user_token }}",
                cache: false,
                dataType: "json",
                contentType : 'application/json',
                processData: false,
                success: function (json) { 
                  console.log(json);
                },
                error: function (error) { 
                  console.log(error);
                }
            });
        });


        jQuery('#close').click(function () {
            $.ajax({
                type: "PUT",
                data: widget_closed_data,
                url: "https://stagingserver.xyz/api/widgets/{{ object.pk }}/?token={{ user_token }}",
                cache: false,
                dataType: "json",
                contentType : 'application/json',
                processData: false,
                success: function (json) { 
                  console.log(json);
                },
                error: function (error) { 
                  console.log(error);
                }
            });
        });

        alert('ready');
        console.log('fuck that shit!')
    });
}

})(); // We call our anonymous function immediately


