document.addEventListener("DOMContentLoaded", function(event) { 
    var imgEl = document.createElement('img');
    imgEl.setAttribute('class', 'logo-image');
    imgEl.setAttribute('src', 'https://www.coveo.com/public/img/coveo_logo.svg');
    imgEl.setAttribute('alt', 'coveo logo');
    
    var parentEl = document.getElementsByClassName('wy-side-nav-search')[0];
    parentEl.insertBefore(imgEl, parentEl.firstChild);
});