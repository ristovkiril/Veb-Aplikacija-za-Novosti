console.log("WOW");
$(document).ready(function () {

    console.log("loaded");

    $('.page-1').show();
    $('.page-2').hide();


    $('#first-page').click(function () {

        $('.page-1').show();
        $('.page-2').hide();
        $('#previous').disable;
        $('#next').enable;

    });

    $('#second-page').click(function () {
        $('.page-2').show();
        $('.page-1').hide();
        $('#next').disable;
        $('#previous').enable;


    });

    $('#previous').click(function () {
        if ($('.page-1').is(':hidden')){
            $('.page-1').show();
            $('.page-2').hide();
            $('#previous').disable;
            $('#next').enable;

        }
    });

    $('#next').click(function () {
        console.log($('.page-2').hidden);
        if ($('.page-2').is(':hidden')){
            $('.page-2').show();
            $('.page-1').hide();
            $('#previous').enable;
            $('#next').disable;

        }
    });
});
