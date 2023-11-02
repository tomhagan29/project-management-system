function toggleClass(projectId) {
  var elements = document.getElementsByTagName("a");

  for (var i = 0; i < elements.length; i++) {
    var element = elements[i];
    if (element.classList.contains("active")) {
      element.classList.remove("active");
    }
  }

  var element = document.getElementById(projectId);
  element.classList.toggle("active");
}

function newProject() {
  var url = document
    .getElementById("new-project-button")
    .getAttribute("data-url");
  window.location.href = url;
}
