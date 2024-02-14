let users = [
    {
        'email': 'admin@admin.com',
        'password': '1234aA!@'
    },
    {
        'email': 'user@gmail.com',
        'password': '11111aA!'
    }
]

const form = document.querySelector('form.login')

form.addEventListener('submit', (e) => {
    e.preventDefault();
    let userMatch = false;
    users.forEach((user) => {
        console.log(user.email);
        console.log(user.password);
        if (form.elements.email.value === user.email && form.elements.password.value === user.password) {
            form.submit();
            userMatch = true;
        }
    })
    if (!userMatch){
            alert("Please check your email and password and try again.")
    }
})