// script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        const inputs = form.querySelectorAll("input");
        let valid = true;

        inputs.forEach((input) => {
            if (input.value.trim() === "") {
                input.classList.add("is-invalid");
                valid = false;
            } else {
                input.classList.remove("is-invalid");
            }
        });

        if (!valid) {
            e.preventDefault(); // Prevent form from submitting
            alert("Please fill in all fields correctly.");
        }
    });
});
