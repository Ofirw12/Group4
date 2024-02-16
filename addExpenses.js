const form = document.querySelector("form.form.addExpenses")
const sendMessage = (message) => {
    const msg = document.querySelector(".msg")
    msg.textContent = message;
    msg.classList.add("msg-error")
    setTimeout(() => {
        msg.classList.remove('msg-error')
        msg.textContent = ''
    }, 4000)
}

const validateForm = (form) => {
    const fields = {
        exType: form.elements.eType,
        category: form.elements.category,
        date: form.elements.date,
        price: form.elements.price,
    };
    if (!fields.exType.value) {
        const message = "Please enter an expense type for your budget.";
        sendMessage(message);
        return false;
    }
    if (!fields.category.value) {
        const message = "Please enter a category for your budget.";
        sendMessage(message);
        return false;
    }
    if (!fields.date.value) {//in the future we will check if the date is in the boundaries of the budget through the backend
        const message = "Please enter a date for your budget.";
        sendMessage(message);
        return false;
    }
    if (fields.price.value <= 0) {
        const message = "Price must be greater than 0.";
        sendMessage(message);
        return false;
    }
    return true;
}
form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (validateForm(form)) {
        form.submit();
    }
})