const form = document.querySelector("form.form.newBudget")


const validateForm = (form) => {
    const fields = {
        budgetName: form.elements.budgetName,
        startDate: form.elements.sDate,
        endDate: form.elements.eDate,
        budget: form.elements.budget,
    };

    let isValid = true;
    const startDate = new Date(fields.startDate.value).setHours(0, 0, 0, 0);
    const endDate = new Date(fields.endDate.value).setHours(0, 0, 0, 0);


    // Name validation
    if (!fields.budgetName.value) {//in the future we will check if the value is unique
        isValid = false;
        alert("Please enter a name for your budget.");
    }

    if (startDate < new Date().setHours(0, 0, 0, 0)) {
        isValid = false;
        alert("Please enter present or future date.");
    }
    if (endDate < startDate) {
        isValid = false;
        alert("Last time I checked, time doesn't work like this.\n end date must be after start date.");
    }
    if (fields.budget.value <= 0) {
        isValid = false;
        alert("Budget must be greater than 0.")

    }

    return isValid;
}
form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (validateForm(form)) {
        form.submit();
    }
})