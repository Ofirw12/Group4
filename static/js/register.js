const form = document.querySelector("form.form.register")

//Validation Message
const sendMessage = (message) => {
    const msg = document.querySelector(".msg")
    msg.textContent = message;
    msg.classList.add("msg-error")
    setTimeout(() => {
        msg.classList.remove('msg-error')
        msg.textContent = ''
    }, 4000)

}


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
        if (hasSymbol && hasLowercase && hasNumber && hasUppercase) {
            break;
        }
    }
    if (!hasSymbol) {
        const message = "Please add at least one symbol character to your password";
        sendMessage(message);
        return false;
    }
    if (!hasNumber) {
        const message = "Please add at least one number character to your password";
        sendMessage(message);
        return false;
    }
    if (!hasUppercase) {
        const message = "Please add at least one upper case character to your password";
        sendMessage(message);
        return false;
    }
    if (!hasLowercase) {
        const message = "Please add at least one lower case character to your password"
        sendMessage(message)
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
        if (!hasLetter) {
            const message ="There is no occupation without a single letter in it's name, please try again."
            sendMessage(message)
            return false;
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
        const message = "Please enter a password with at least 8 characters.";
        sendMessage(message);
        return false;
    } else {
        isValid = validatePassword(fields.password.value);
    }

    // Name validation
    if (!fields.lName.value) {
        const message = "Please enter your first and last name.";
        sendMessage(message);
        return false;
    }
    if (!fields.fName.value) {
        const message = "Please enter your first name.";
        sendMessage(message);
        return false;
    }

    // Age validation
    if (fields.age.value <= 0) {
        const message = "This can't be right, please check the age you've entered and try again.";
        sendMessage(message);
        return false;
    } else if (fields.age.value < 18) {
        const years = 18 - parseInt(fields.age.value);
        const message = `You're too young for this site, come back again in ${years} years.`;
        sendMessage(message);
        return false;
    } else if (fields.age.value > 120) {
        const message = "Please enter a valid age between 18 and 120.";
        sendMessage(message);
        return false;
    }

    // Gender validation
    if (fields.gender.value === "") {
        const message = "Please select your gender.";
        sendMessage(message);
        return false;
    }
    // Optional occupation validation
    if (fields.occupation.value) {
        isValid = validateOccupation(fields.occupation.value);
    }
    return isValid;
}
form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (validateForm(form)) {
        form.submit();
    }
})