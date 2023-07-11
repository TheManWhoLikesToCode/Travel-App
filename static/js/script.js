const form = document.getElementById("destination-form");
const list = document.getElementById("destinations-list");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const destination = document.getElementById("destination-input").value;
  const listItem = document.createElement("li");
  listItem.textContent = destination;
  list.appendChild(listItem);
  form.reset();
});
