// process bar function
var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 10;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
        elem.innerHTML = width  + "%";
      }
    }
  }
}

// for delete onclick function
$(function() {
  $('a#delete_btn').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/upload result',
        function(data) {
      //do nothing
    });
    return false;
  });
});