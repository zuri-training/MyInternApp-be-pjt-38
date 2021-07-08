const form = document.getElementById("signup_form");
const firstName = document.getElementById("first_name");
const lastName = document.getElementById("last_name");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
const country = document.getElementById("country");
const city = document.getElementById("city");
const business = document.getElementById("business");
const role = document.getElementById("role");
const address = document.getElementById("address");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");
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
	const emailValue = email.value.trim();
	const phoneValue = phone.value.trim();
	const countryValue = country.value.trim();
	const cityValue = city.value.trim();
	const businessValue = business.value.trim();
	const roleValue = role.value.trim();
	const addressValue = address.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();

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

	// Check Email
	if (emailValue === "") {
		setErrorFor(email, "Email cannot be blank");
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, "Please enter a valid email");
	} else {
		setSuccessFor(email);
	}

	// Check Number
	if (phoneValue === "") {
		setErrorFor(phone, "Phone number cannot be blank");
	} else {
		setSuccessFor(phone);
	}

	// Check country
	if (countryValue === "") {
		setErrorFor(country, "Please select a country");
	} else {
		setSuccessFor(country);
	}

	// Check City
	if (cityValue === "") {
		setErrorFor(city, "Please enter a city");
	} else {
		setSuccessFor(city);
	}

	// Check business
	if (businessValue === "") {
		setErrorFor(business, "School cannot be blank");
	} else {
		setSuccessFor(business);
	}

	// Check role
	if (roleValue === "") {
		setErrorFor(role, "Please select a role");
	} else {
		setSuccessFor(role);
	}

	// Check addresss
	if (addressValue === "") {
		setErrorFor(address, "Please enter a address");
	} else {
		setSuccessFor(address);
	}

	// Check passwords
	if (passwordValue === "") {
		setErrorFor(password, "Password cannot be blank");
	} else {
		setSuccessFor(password);
	}

	// Check password2
	if (password2Value === "") {
		setErrorFor(password2, "Password confirmation is required");
	} else if (password2Value !== passwordValue) {
		setErrorFor(password2, "Passwords do not match");
	} else {
		setSuccessFor(password);
	}

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

// Check for valid email
function isEmail(email) {
	const re =
		/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(String(email).toLowerCase());
}
