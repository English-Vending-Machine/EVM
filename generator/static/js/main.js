$(document).ready(function() {
       var $header = $('.header');
       var $hbEl = $('html, body');
       var $body = $('body');

       $('.page_admin .member_info').on('click', function() {
              $(this).parent().toggleClass('on');
       });


});