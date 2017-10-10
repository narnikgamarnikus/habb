window.onload = function() {
    if (!window.jQuery) {
        var script = document.createElement('script');
        script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
        document.body.appendChild(script);
    }

    var iframe = document.createElement('iframe');
    iframe.id = 'widget';
    iframe.frameBorder = 0;
    iframe.src = 'https://stagingserver.xyz/ru/widget/';
    document.body.appendChild(iframe);

    window.addEventListener('message', function (event) {
        var widget = $('#widget');
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