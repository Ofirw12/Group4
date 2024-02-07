const selectElement = document.querySelector('.confirm-deny');

selectElement.addEventListener('change', (e) => this.form.submit());

const friendsList = document.querySelector('my-friends-list')
const countOfFriends = document.getElementById('total')
const rows = document.querySelectorAll('.friendRow')
const count = () =>{
    let total = 0;
    rows.forEach((row) => total += 1);
    return total;
}

countOfFriends.textContent = count();