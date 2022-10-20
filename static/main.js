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
function delete_file(e){
  //getting the parent element's text(<li> text)
  let selectedfile = e.parentElement.innerText;
  console.log(selectedfile)

  //removing the chosen from the UI
  e.parentElement.innerText = '';

  const request = new XMLHttpRequest();
  request.open('POST', `/ProcessSelectedfile/${JSON.stringify(selectedfile)}`)
  request.send();
}

//function to load from upload page to next page
function from_upload_page_next(){
  window.location.href = "templates/folders choice.html";
}

//function to load from upload page to back page
function from_upload_page_back(){
  window.location.href = "templates/start.html";
}