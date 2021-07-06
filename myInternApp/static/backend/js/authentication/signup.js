const form = document.getElementById("signup_form");
const firstName = document.getElementById("first_name");
const lastName = document.getElementById("last_name");
const userType = document.getElementById("user_type");
const genders = document.getElementsByName("gender");
const genderInput = document.querySelector(".gender-input");

form.addEventListener("submit", (e) => {
	e.preventDefault();

	// Validate form inputs
	validateForm();
});

// Validate Form Inputs Function
function validateForm() {
	// get the values from the inputs
	const firstNameValue = firstName.value.trim();
	const lastNameValue = lastName.value.trim();
	const userTypeValue = userType.value.trim();

	// Check Firstname
	if (firstNameValue === "") {
		setErrorFor(firstName, "First name cannot be blank");
	} else {
		setSuccessFor(firstName);
	}

	// Check Firstname
	if (lastNameValue === "") {
		setErrorFor(lastName, "Last name cannot be blank");
	} else {
		setSuccessFor(lastName);
	}

	// Check Type of User
	if (userTypeValue === "") {
		setErrorFor(userType, "Please select a type of user");
	} else {
		setSuccessFor(userType);
		nextPage(userTypeValue);
	}

	// Check for Gender of User
	// if (gender === null) {
	// 	// setErrorFor(genderInput, "Please select a gender");
	// 	alert("gender");
	// }

	if (genders[0].checked === true) {
		setSuccessFor(genderInput);
		return true;
	} else if (genders[1].checked === true) {
		setSuccessFor(genderInput);

		return true;
	} else {
		// no checked
		setErrorFor(genderInput, "Please select a gender");
		return false;
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

// Next page
function nextPage(userType) {
	switch (userType) {
		case "Student":
			window.location = "./student-signup.html";
			break;
		case "Employer":
			window.location = "./employer-signup.html";
			break;

		default:
			window.location = "signup.html";
			break;
	}
}
