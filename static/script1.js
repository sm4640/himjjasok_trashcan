function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var draggedImage = document.getElementById(data);
    ev.target.appendChild(draggedImage);

    var opacity = 1;
    var intervalId = setInterval(function () {
        if (opacity <= 0) {
            clearInterval(intervalId);
            draggedImage.style.display = "none";
            document.getElementById("button").style.display = "block";
        } else {
            opacity -= 0.1;
            draggedImage.style.opacity = opacity;
        }
    }, 100);
}
function changePage() {
    window.location.href = "cookie1";
}
