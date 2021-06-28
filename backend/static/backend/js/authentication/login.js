const form = document.getElementById("login_form");
const email = document.getElementById("login_email");
const password = document.getElementById("login_password");

form.addEventListener("submit", (e) => {
	// e.preventDefault();

	validateForm();
});

// Validate Form Inputs Function
function validateForm() {
	// get the values from the inputs
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();

	if (emailValue === "") {
		setErrorFor(email, "Email cannot be blank");
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, "Please enter a valid email");
	} else {
		setSuccessFor(email);
	}

	if (passwordValue === "") {
		setErrorFor(password, "Password cannot be blank");
	} else {
		setSuccessFor(password);
	}
}

// Set Error Class Function
function setErrorFor(input, message) {
	const formInputContainer = input.parentElement;
	const errorMessage = formInputContainer.querySelector(".error-message");

	// add error message inside error message class
	errorMessage.innerText = message;

	// add error class to input
	formInputContainer.classList.add("error");
}

// Remove Error class from input
function setSuccessFor(input) {
	const formInputContainer = input.parentElement;

	// add error class to input
	formInputContainer.classList.remove("error");
}

// Check for valid email
function isEmail(email) {
	const re =
		/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(String(email).toLowerCase());
}
