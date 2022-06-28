// Slider functions on index.html page
$(document).ready(function(){
    $('.slick1').slick({
        Infinite: true, 
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1000,
        dots: true
});
});

$(document).ready(function(){
    $('.slick2').slick({
        Infinite: true, 
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1000,
        dots: true
});
});


// Activate select fields on online_queue.html page
function activateServiceOptions(){
    document.getElementById('service-options').removeAttribute('disabled'); 
}
function activateDateTimeOptions(){
    document.getElementById('date-options').removeAttribute('disabled'); 
    document.getElementById('time-options').removeAttribute('disabled') ;
}

// Search function on search.html
$(document).ready(function(){
    if (document.getElementById('result-count') !== null){
        document.getElementById('result-count').innerHTML = document.getElementsByClassName('search-result').length
    }
 });