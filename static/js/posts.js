// //////////////////
// JavaScript for posts page
// ////////////////

$(function(){
    // Executed when js_menu-icon js clicked
    $('.js-menu-icon').click(function() {
        // $this : Self element, namely div.js-menu-icon
        // next() : Next to div.js-menu-icon, namely div.menu
        //  toggle():
        $(this).next().toggle();
    })
})