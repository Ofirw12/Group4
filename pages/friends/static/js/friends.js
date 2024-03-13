const sum = () => {
    const friend_rows = document.querySelectorAll('tr.friendRow')
    const total_cell = document.querySelector('#total')
    let total = 0
    friend_rows.forEach((row) => {
        total += 1
    })
    total_cell.textContent = total
}
window.addEventListener("load", (e) => {
    count()
})

testclick = document.getElementById('testclick')
console.log('Hi')
testclick.addEventListener('click', (e) => {

    count()
})

const total_cell = document.querySelector('#table_list')
const tbodyRowCount = table_list.tBodies[0].rows.length; // 3
const count = () => {
const total_cell = document.querySelector('#table_list')
const tbodyRowCount = total_cell.tBodies[0].rows.length; // 3
    total_cell.textContent = tbodyRowCount.toString()
}