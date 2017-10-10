window.onload = function() {
    if (!window.jQuery) {
        var script = document.createElement('script');
        script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
        document.body.appendChild(script);
    }

    var iframe = document.createElement('iframe');
    iframe.id = 'it-zombie-widget';
    iframe.frameBorder = 0;
    iframe.src = 'https://stagingserver.xyz/ru/widget/';
    document.body.appendChild(iframe);

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
        if (event.data.token === "123456") {
            if (event.data.event === 'open') {
                widget.css('height', '100%');
                widget.css('width', '100%');
                $('body').css('overflow', 'hidden');
            }
            if (event.data.event === 'close') {
                widget.css('height', '160');
                widget.css('width', '180');
                $('body').css('overflow', 'visible');
            }
        }
    }, false);
};