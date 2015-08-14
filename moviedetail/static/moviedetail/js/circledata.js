
$(document).ready(function() {
    var circle_divs = $(".prec");


    for (var i=0; i<circle_divs.length; i++) {
        var circle = circle_divs[i];

        var deg = circle.innerHTML;
        var degNum = deg.substring(0, deg.length - 1);
        var activeBorder = circle.parentNode.parentNode;
        // alert(activeBorder.nodeName);
        if (degNum <= 180){
            activeBorder.style.backgroundImage = 'linear-gradient(' + (+90 + +degNum) + 'deg, transparent 50%, #A2ECFB 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)';
            // activeBorder.css('background-image','linear-gradient(' + (90+degNum) + 'deg, transparent 50%, #A2ECFB 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
        } else {
            activeBorder.style.backgroundImage = 'linear-gradient(' + (+degNum - +90) + 'deg, transparent 50%, #39B4CC 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)';
            // activeBorder.css('background-image','linear-gradient(' + (degNum-90) + 'deg, transparent 50%, #39B4CC 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
        }
    }

});







