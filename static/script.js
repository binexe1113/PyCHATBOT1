const userInput = document.getElementById("user-input");

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  appendMessage("Você", message);
  input.value = "";

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  appendMessage("Robo do horário", data.response);
}

function appendMessage(sender, text) {
  const messages = document.getElementById("messages");
  const div = document.createElement("div");
  div.innerHTML = `<b>${sender}:</b> ${text}`;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

userInput.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    event.preventDefault();
    sendMessage();
  }
});


window.addEventListener("DOMContentLoaded", () => {
  appendMessage("Robo do horário", "Olá! Eu Sou um robo que pode te dizer o horário oficial de brasilia!\nMe pergunte às horas ");
});
