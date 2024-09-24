// Change web mode to dark mode with button click event
// and vice-versa

/* global $ */
$(document).ready(() => {
    $('.darkmode').click(function() {
        if ($('body').hasClass('dark')) {
            /* revert it back to normal mode */
            $('body').removeClass('dark');
            $('body').css('background-color', 'rgb(224, 217, 217)');
            $('h1, h2').css('color', '#000000');
            $('.darkmode').text('Dark Mode');
        } else {
            /* switch to dark mode */
            $('body').addClass('dark');
            $('body').css('background-color', '#000000');
            $('h1, h2').css('color', '#000000');
            $('.darkmode').text('Light Mode');
        }
    });
});