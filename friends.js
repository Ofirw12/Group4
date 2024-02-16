const responses = document.querySelectorAll('.confirm-deny');
const form = document.querySelector('.quick-form')
const friendsList = document.querySelector('.my-friends-list')

class Friend {
    constructor(email, fName, lName, friendsSince) {
        this.email = email;
        this.fName = fName;
        this.lName = lName;
        this.friendsSince = friendsSince;
    }
}
const count = () => {
    const countOfFriends = document.getElementById('total')
    const rows = document.querySelectorAll('.friendRow')
    let total = 0;
    rows.forEach((row) => total += 1);
    countOfFriends.textContent = total;
}

let friends = [
    new Friend('moshetheking5@gmail.com', 'Moshe', 'Simha', 2005),
    new Friend('ItzikKL@yahoo.com', 'Itzik', 'Kalahani', 2023)
]

const addRows=(list)=>{
    list.forEach((friend) => {
    const newRow = friendsList.insertRow(1)
    newRow.classList.add("friendRow")
    newRow.insertCell(0).textContent = friend.email;
    newRow.insertCell(1).textContent = friend.fName;
    newRow.insertCell(2).textContent = friend.lName;
    newRow.insertCell(3).textContent = friend.friendsSince
})
    count();
}
addRows(friends);

responses.forEach((response) => {
    response.addEventListener('change', (e) => {
        e.preventDefault();
        const row = response.closest('tr');
        friendsList.insertRow(1)
        if (e.target.value === 'confirm') {
            const newFriend = new Friend(row.cells[0].textContent, row.cells[1].textContent, row.cells[2].textContent, new Date().getFullYear());
            friends.push(newFriend);
            const friendRows =document.querySelectorAll('.friendRow');
            friendRows.forEach((friend)=>{
                friend.remove();
            })
            addRows(friends);
            row.remove();
            count();
        } else if (e.target.value === 'deny') {
            row.remove();
        }
    });
})

