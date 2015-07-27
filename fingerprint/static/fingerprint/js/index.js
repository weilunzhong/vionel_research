var src = 0

function select() {
    src = event.target.src
    document.getElementById("target").innerHTML = document.getElementById("target").innerHTML + '<img src="' + src + '"  width="120" height="160">';
    var max = document.getElementById("target").childNodes.length;
    if (max > 2) {
        document.getElementById("target").innerHTML = '<img src="' + src + '"  width="120" height="160px">'
    }
}

function reset() {
    addmovie()
    alert(document.getElementById("moviefingerprint1").childNodes.length)
    my_time = setTimeout('timer()', 2);
    clearTimeout(my_time);
    var elems = document.getElementsByClassName('moving');
    for (var i = 0; i < elems.length; i++) {
        elems[i].style.top = 300 - elems[i].height / 2 + "px";
    }

    document.getElementById("msg").innerHTML = "";

}

var step = 1


function disp() {

    step = step + 1;
    //var step=1; // Change this step value
    //alert("Hello");
    var elems = document.getElementsByClassName('moving');

    for (var i = 0; i < elems.length; i++) {
        //alert(elems[i].height);  
        var y = elems[i].offsetTop;
        var x = elems[i].offsetLeft;
        //elems[i].height=elems[i].height/2
        // alert(x + "tt" + y);
        y = 150 - elems[i].height / 2 + 100 * elems[i].height / 400 * Math.sin(step * elems[i].height * Math.PI / 5000);
        // document.getElementsByClassName('moving')[i].style.top = y + "px"; // vertical movment
        elems[i].style.top = y + "px";
    }

    if (step == 10000) {
        step = 0;
    }
    //////////////////////

}

function timer() {
    disp();
    //var y=document.getElementsByClassName('moving')[0].offsetTop;
    //var x=document.getElementsByClassName('moving')[0].offsetLeft;
    //document.getElementById("msg").innerHTML="X: " + x + " Y : " + y
    my_time = setTimeout('timer()', 2);
}


function checkImage(src) {
    var img = new Image();
    img.onload = function() {
        alert('1');
    };
    img.onerror = function() {
        alert('0');
    };

    img.src = src; // fires off loading of image
}


// OK
function addsilent() {
    var src = document.getElementById("moviefingerprint1");
    var img = document.createElement("img");
    var selected = document.getElementById("target").childNodes;
    dir1 = selected[0].src.replace(".jpg", "/");
    img.src = dir1 + "resize.jpg";
    img.setAttribute("class", "moving item");
    img.id = "big1"
        //img.setAttribute("id", "big");
    img.width = 1200
    img.height = 300
    img.setAttribute("onmouseover", "showtrail()");
    img.setAttribute("onmouseout", "hidetrail()");
    //img.setAttribute("width", "1600px");      
    src.appendChild(img);

    var src = document.getElementById("moviefingerprint2");
    var img = document.createElement("img");
    dir2 = selected[1].src.replace(".jpg", "/");
    img.src = dir2 + "resize.jpg";
    img.setAttribute("class", "moving item");
    img.id = "big2"

    img.width = 1200
    img.height = 300
    img.setAttribute("onmouseover", "showtrail()");
    img.setAttribute("onmouseout", "hidetrail()");

    src.appendChild(img);
}


var sign = 0

function adddynamic() {
    var src = document.getElementById("moviefingerprint1");
    num = 0

    var selected = document.getElementById("target").childNodes;
    var selectedList = selected[0].src.replace(".jpg", "").split('/');
    var title = selectedList[selectedList.length - 1];

    if (title == 'James%20Bond%20Casino%20Royale%20(2006)') {
        //alert('good');
        num = 15
    }
    if (title == 'James%20Bond%20Die%20Another%20Day%20(2002)') {
        //alert('good');
        num = 31
    }
    if (title == 'The%20Illusionist%20(2006)') {
        //alert('good');
        num = 20
    }
    if (title == 'The%20Prestige%20(2006)') {
        //alert('good');
        num = 23
    }
    if (title == 'Alien%20Directors%20Cut%20(1979)') {
        //alert('good');
        num = 39
    }
    if (title == '2001%20A%20Space%20Odyssey%20(1968)') {
        //alert('good');
        num = 33
    }
    if (title == 'Rocky%20(1976)') {
        //alert('good');
        num = 19
    }
    if (title == 'Rocky%20III%20(1982)') {
        //alert('good');
        num = 15
    }

    for (var i = 0; i < num; i++) {
        var img = document.createElement("img");
        img.src = selected[0].src.replace(".jpg", "/") + "resized/chapter" + i + ".jpg";
        img.setAttribute("class", "moving item");
        src.appendChild(img);
    }


    var src = document.getElementById("moviefingerprint2");
    num = 0

    var selected = document.getElementById("target").childNodes;
    var selectedList = selected[1].src.replace(".jpg", "").split('/');
    var title = selectedList[selectedList.length - 1];

    if (title == 'James%20Bond%20Casino%20Royale%20(2006)') {
        //alert('good');
        num = 15
    }
    if (title == 'James%20Bond%20Die%20Another%20Day%20(2002)') {
        //alert('good');
        num = 31
    }
    if (title == 'The%20Illusionist%20(2006)') {
        //alert('good');
        num = 20
    }
    if (title == 'The%20Prestige%20(2006)') {
        //alert('good');
        num = 23
    }
    if (title == 'Alien%20Directors%20Cut%20(1979)') {
        //alert('good');
        num = 39
    }
    if (title == '2001%20A%20Space%20Odyssey%20(1968)') {
        //alert('good');
        num = 33
    }
    if (title == 'Rocky%20(1976)') {
        //alert('good');
        num = 19
    }
    if (title == 'Rocky%20III%20(1982)') {
        //alert('good');
        num = 15
    }

    for (var i = 0; i < num; i++) {
        var img = document.createElement("img");
        img.src = selected[1].src.replace(".jpg", "/") + "resized/chapter" + i + ".jpg";
        img.setAttribute("class", "moving item");
        src.appendChild(img);
    }
}