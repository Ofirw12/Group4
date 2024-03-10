const form = document.querySelector("form.form.newBudget")

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
        budgetName: form.elements.budgetName,
        startDate: form.elements.sDate,
        endDate: form.elements.eDate,
        budget: form.elements.budget,
    };
    const startDate = new Date(fields.startDate.value).setHours(0, 0, 0, 0);
    const endDate = new Date(fields.endDate.value).setHours(0, 0, 0, 0);
    // Name validation
    if (!fields.budgetName.value) {//in the future we will check if the value is unique
        const message = "Please enter a name for your budget.";
        sendMessage(message);
        return false;
    }
    if (startDate < new Date().setHours(0, 0, 0, 0)) {
        const message = "Please enter present or future date.";
        sendMessage(message);
        return false;
    }
    if (endDate < startDate) {
        const message = "Last time I checked, time doesn't work like this.\nend date must be after start date.";
        sendMessage(message);
        return false;
    }
    if (fields.budget.value <= 0) {
        const message = "Budget must be greater than 0.";
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