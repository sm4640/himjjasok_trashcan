var images = [
    "{% static 'beforeFall.png' %}",
    "{% static 'fallBoo.png' %}",
    "{% static 'cookie.png' %}",
];
var currentIndex = 0;

function changeImage() {
    var image = document.getElementById("myImage");

    if (currentIndex < images.length - 1) {
        currentIndex++;
        image.src = images[currentIndex];
        // console.log(image.src);
    } else if (currentIndex === images.length - 1) {
        // 이미지가 3번째 이미지일 경우 다른 HTML 파일로 이동
        window.location.href = "cookie2";
    }
}
