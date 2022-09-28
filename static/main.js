function update() {
  var element = document.getElementById("myprogressbar");
  var width = 1;
  var indetity = setInterval(scene, 10);
  function scene() {
    if (width >= 10) {
      clearInterval(indetity);
    }
    else {
      width++;
      element.style.width = width + '%';
    }
  }
}