window.onload = function() {
    // if the site does not have jquery - connect it
    if (!window.jQuery) {
        var script = document.createElement('script');
        script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
        document.body.appendChild(script);
    }

    function S4() {
        return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
    }

    const token = (S4() + S4() + "-" + S4() + "-4" + S4().substr(0,3) + "-" + S4() + "-" + S4() + S4() + S4()).toLowerCase();

    // add input for storage token on user site
    var input = document.createElement('input');
    input.type = 'hidden';
    input.id = 'lead-zombie-token';
    input.value = token;
    document.body.appendChild(input);

    // add frame for widget on user site
    var iframe = document.createElement('iframe');
    iframe.id = 'it-zombie-widget';
    iframe.frameBorder = 0;
    iframe.src = 'https://stagingserver.xyz/ru/widget/';
    document.body.appendChild(iframe);

    // add widget styles on user site
    var css = '#it-zombie-widget { position: fixed; top: 0; left: 0; margin: 0; padding: 0; width: 180px; height: 160px; }',
        head = document.head || document.getElementsByTagName('head')[0],
        style = document.createElement('style');

    style.type = 'text/css';
    if (style.styleSheet){
        style.styleSheet.cssText = css;
    } else {
        style.appendChild(document.createTextNode(css));
    }
    head.appendChild(style);

    window.addEventListener('message', function (event) {
        var widget = $('#it-zombie-widget');
        if (event.data.token === 'it-zombie') {
            if (event.data.event === 'open') {
                widget.css('height', '100%');
                widget.css('width', '100%');
                $('body').css('overflow', 'hidden');
            }
            if (event.data.event === 'it-zombie') {
                widget.css('height', '160');
                widget.css('width', '180');
                $('body').css('overflow', 'visible');
            }
        }
    }, false);
};