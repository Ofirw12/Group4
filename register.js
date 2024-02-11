const form = document.querySelector("form.form.register")

//Password validation
const validatePassword = (password) => {
    let hasLowercase = false;
    let hasUppercase = false;
    let hasNumber = false;
    let hasSymbol = false;

    for (let i = 0; i < password.length; i++) {
        const char = password[i];

        // Check for lowercase letter by ASCII codes (a-z)
        if (char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122) {
            hasLowercase = true;
        }

        // Check for uppercase letter by ASCII codes (A-Z)
        if (char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) {
            hasUppercase = true;
        }

        // Check for number by ASCII codes (0-10)
        if (char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57) {
            hasNumber = true;
        }

        // Check for symbol by ASCII codes
        if ((char.charCodeAt(0) >= 33 && char.charCodeAt(0) <= 47) ||
            (char.charCodeAt(0) >= 58 && char.charCodeAt(0) <= 64) ||
            (char.charCodeAt(0) >= 91 && char.charCodeAt(0) <= 96) ||
            (char.charCodeAt(0) >= 123 && char.charCodeAt(0) <= 126)) {
            hasSymbol = true;
        }
        if (hasSymbol && hasLowercase && hasNumber && hasUppercase){
            break;
        }
    }
    if (!hasSymbol) {
        alert("Please add at least one symbol character to your password")
        return false;
    }
    if (!hasNumber) {
        alert("Please add at least one number character to your password")
        return false;
    }
    if (!hasUppercase) {
        alert("Please add at least one upper case character to your password")
        return false;
    }
    if (!hasLowercase) {
        alert("Please add at least one lower case character to your password")
        return false;
    }
    return true;
}

const validateOccupation = (occupation) => {
    if (occupation) {
        let hasLetter = false;
        for (let i = 0; i < occupation.length; i++) {
            const char = occupation[i]
            // Check for lowercase letter by ASCII codes (a-z)
            if (char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122) {
                hasLetter = true;
                break;
            }

            // Check for uppercase letter by ASCII codes (A-Z)
            if (char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) {
                hasLetter = true;
                break;
            }
        }
        if (!hasLetter){
            alert("There is no occupation without a single letter in it's name, please try again.")
        }
        return hasLetter;


    }
    return true;
}

const validateForm = (form) => {
    const fields = {
        password: form.elements.password,
        fName: form.elements.fName,
        lName: form.elements.lName,
        age: form.elements.age,
        gender: form.elements.gender,
        occupation: form.elements.occupation,
    };

    let isValid = true;

    if (fields.password.value.length < 8) {
        isValid = false;
        alert("Please enter a password with at least 8 characters.");
    } else {
        isValid = validatePassword(fields.password.value);
    }

    // Name validation
    if (!fields.lName.value) {
        isValid = false;
        alert("Please enter your first and last name.");
    }
    if (!fields.fName.value) {
        isValid = false;
        alert("Please enter your first name.");
    }

    // Age validation
    if (fields.age.value <= 0) {
        isValid = false;
        alert("This can't be right, please check the age you've entered and try again.")
    } else if (fields.age.value < 18) {
        isValid = false;
        const years = 18 - parseInt(fields.age.value)
        alert(`You're too young for this site, come back again in ${years} years.`)
    } else if (fields.age.value > 120) {
        isValid = false;
        alert("Please enter a valid age between 18 and 120.");
    }

    // Gender validation
    if (fields.gender.value === "") {
        isValid = false;
        alert("Please select your gender.");
    }
    // Optional occupation validation
    isValid = validateOccupation(fields.occupation.value);

    return isValid;
}
form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (validateForm(form)) {
        form.submit();
    }
})