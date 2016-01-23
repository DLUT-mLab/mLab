var nav_margin_btm = 21;

$(window).resize(function() {
    var scrollTop = 0;
    var hh = $('header').height();
    var bannerHeight = $('.header-banner').height();
    window.onscroll = function() {
        scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
        if (scrollTop > bannerHeight) {
            $('.content-wrap').css('padding-top', hh + nav_margin_btm);
            $('.header-menu').css('position', 'fixed');
            $('.header-banner').hide();
        } else {
            $('.content-wrap').css('padding-top', '0px');
            $('.header-menu').css('position', '');
            $('.header-banner').show();
        }
    }
});

$(document).ready(function() {
    var content_height = $(window).height() - $('header').height() - $('.footer').height() - nav_margin_btm - 15;
    $('.content-wrap').css('min-height', content_height);
    $.each($('.navbar-nav').find('li'), function() {
        console.log(window.location.pathname);  
        $(this).toggleClass('active',
            $(this).find('a').attr('href') == window.location.pathname);
    });
    $(window).resize();
});