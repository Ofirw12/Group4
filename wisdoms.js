const prices = document.querySelectorAll('.price')

function sum() {
    let total = 0;
    prices.forEach((price) => total += parseInt(price.textContent))
    return total;
}

document.getElementById('totalPrice').textContent = sum();
// if (sum()>1000){
//     document.getElementById('totalPrice').style.backgroundColor = `red`;
// }