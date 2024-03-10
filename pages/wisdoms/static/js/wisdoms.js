// const prices = document.querySelectorAll('.price')

const sum =() =>{
    let total = 0;
    const prices = document.querySelectorAll('.price')
    prices.forEach((price) => total += parseInt(price.textContent))
document.querySelector('#totalPrice').textContent =total;

}


class Expense {
    constructor(category, expenseType, date, price) {
        this.category = category;
        this.expenseType = expenseType;
        this.date = date;
        this.price = price;
    }
}

let expenses = [
    new Expense("Shopping", "Shoes", "1/2/2022", 300),
    new Expense("Shopping", "Dress", "1/3/2023", 852),
    new Expense("Shopping", "Coffee", "6/2/2021", 15),
    new Expense("Education", "Books", "9/2/2021", 455),
    new Expense("Education", "ChatGPT", "14/2/2024", 17),
    new Expense("Education", "Tutors", "9/9/2021", 1000),
    new Expense("Bills", "Water bill", "10/1/2023", 321),
    new Expense("Bills", "Car insurance", "22/1/2024", 5200),
    new Expense("Bills", "Electricity bill", "8/1/2024", 399),
]

const filterBtn = document.querySelector('.filter');
const WisdomsTable =document.querySelector('.expenses');

// const addRows =(list)=>{
//     list.forEach((expense) => {
//     const newRow = WisdomsTable.insertRow(1)
//     newRow.classList.add("expenseRow")
//     newRow.insertCell(0).textContent = expense.category;
//     newRow.insertCell(1).textContent = expense.expenseType;
//     newRow.insertCell(2).textContent = expense.date;
//     const price = newRow.insertCell(3);
//     price.textContent = expense.price;
//     price.classList.add('price');
//
// })
//     sum();
// }
// addRows(expenses);
// filterBtn.addEventListener('submit',(e)=>{
//     e.preventDefault();
//     const rows = document.querySelectorAll('.expenseRow');
// rows.forEach((expenseRow) =>{
//     expenseRow.remove();
// })
//     const form =document.querySelector('.quick-form.form.filter')
//     let filtered = expenses.filter((expense)=> form.elements.expenseType.value === expense.category
//     )
//     addRows(filtered);
// })
window.addEventListener('load', (e) => {
    sum();
});


