const form = document.querySelector("form.form.addExpenses")

const validateForm = (form) => {
    const fields = {
        exType: form.elements.eType,
        category: form.elements.category,
        date: form.elements.date,
        price: form.elements.price,
    };
    let isValid = true;

    if (!fields.exType.value) {
        isValid = false;
        alert("Please enter an expense type for your budget.");
    }
    if (!fields.category.value) {
        isValid = false;
        alert("Please enter a category for your budget.");
    }
    if (!fields.date.value) {//in the future we will check if the date is in the boundaries of the budget
        isValid = false;
        alert("Please enter a date for your budget.");
    }
    if (fields.price.value <= 0) {
        isValid = false;
        alert("Price must be greater than 0.")

    }

    return isValid;

}
form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (validateForm(form)) {
        form.submit();
    }
})