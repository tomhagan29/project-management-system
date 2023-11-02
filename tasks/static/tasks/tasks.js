function newTask() {
  var url = document.getElementById("new-task-button").getAttribute("data-url");
  window.location.href = url;
}
