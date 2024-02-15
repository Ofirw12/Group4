# BudgetBunny

A web app built using vanilla HTML, CSS and JS by Hila Ziegler and Ofir Wysboom as a part of Web Development Course.

## Client-Side:
each page got a Navbar with useful links, if the user is logged in he will also get a logout link that will take him back to the login page.


### **Login**:
The user can login using these credentials:

```JavaScript
       email: admin@admin.com
        password: 1234aA!@
```

```JavaScript
        email: user@gmail.com
        password: 11111aA!
```

When clicking Submit, the inserted values are being checked to be one of the above, if successful the user will get to the home page.

### **Register**:
On this screen you can register to the system, after checking the form input the user will be sent to the home screen.

### **Home**:
On this screen, the user can choose to add expenses to an existing budget, create a new budget, and view insights on his expenses.

### **Friends**:
A Friends class was created for this page, each row in the top table is based on an instance of a friend. In addition, The lower table resemble friend requests and based on your choice whether to approve/reject a friend request, the upper table will be updated.

### **Wisdoms**:
In this screen, the user can see his recent expenses filtered by category, in addition it presents general insights compared to the user's past, his friends and all users.

### **Add Expenses**:
In this screen, the user will enter a new expense to the selected budget, the inputs he will provide are:
* **Expense Type**: The expense type cannot be empty.
* **Category**: The category cannot be empty.
* **Date**: Any date is accepted.
* **Price**: Must be a positive number greater than 0.

### **New Budget**:
On this screen, the user will create a new budget for himself,
The inputs he will provide are:

* **Budget Name**: The budget name cannot be empty, must have at least one character (a budget with a name that includes only a number is accepted)
* **Start Date**: The date must be present or future days.
* **End Date**: The date must be equal to or greater than the start date of the budget.
* **Budget**: Must be a positive number greater than 0.

