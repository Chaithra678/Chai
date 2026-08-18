async function send(){
  let msg = document.getElementById("msg").value;
  let res = await fetch("https://your-render-app.onrender.com/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: msg})
  });
  let data = await res.json();
  document.getElementById("reply").innerText = data.reply;
}
