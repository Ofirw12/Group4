const date = new Date();
const formatter = new Intl.DateTimeFormat('he-IL', { day: '2-digit', month: '2-digit', year: 'numeric' });
const formattedDate = formatter.format(date);

document.getElementById("date").textContent = formattedDate;
const form= document.querySelector('form.form.add-expense');

form.addEventListener('submit',(e)=>{
    e.preventDefault()
    const budget= form.elements.Budget.value;
    localStorage.setItem('budgetName',JSON.stringify(budget));
    form.submit();
})