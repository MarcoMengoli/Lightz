function loadChores() {
  fetch("/chores") // Modify this if your API endpoint is different
    .then((response) => response.json())
    .then((data) => {
      const choresContainer = document.getElementById("choresContainer");
      data.forEach((choreName) => {
        let button = document.createElement("button");
        button.innerText = choreName;
        button.addEventListener("click", () => setCurrentChore(choreName));
        choresContainer.appendChild(button);
      });
    });
}

function setCurrentChore(name) {
  fetch("/chores", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name: name }),
  }).then((response) => {
    if (response.ok) {
      alert(`Set current chore to: ${name}`);
    } else {
      alert("Failed to set current chore.");
    }
  });
}
