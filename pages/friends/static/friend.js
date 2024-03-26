
const sendMessage = (message) => {
    const msg = document.querySelector(".msg")
    msg.textContent = message;
    msg.classList.add("msg-error")
    setTimeout(() => {
        msg.classList.remove('msg-error')
        msg.textContent = ''
    }, 4000)

}
window.addEventListener("load", (e) => {
    const msg = document.querySelector(".msg").textContent
    if (msg !== ""){
        // document.querySelector(".not_msg").textContent =""
        sendMessage(msg)
    }
})
