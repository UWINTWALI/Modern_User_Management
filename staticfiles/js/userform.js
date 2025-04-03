document.addEventListener("DOMContentLoaded", function () {
    // Apply modal styles
    const modal = document.querySelector(".modal-lg-custom");
    if (modal) {
        modal.style.maxWidth = "100%";
        modal.style.marginTop = "-1rem";
    }

    // Apply modal content styles
    const modalContent = document.querySelector(".modal-content");
    if (modalContent) {
        modalContent.style.padding = "20px";
    }

    // Apply body styles
    // document.body.style.backgroundColor = "var(--background-color)";
    // document.body.style.color = "var(--text-color)";
    // document.body.style.fontFamily = "'Arial', sans-serif";
    // document.body.style.fontSize = "var(--font-size-medium)";
    // document.body.style.lineHeight = "1.5";
    // document.body.style.margin = "0";
    // document.body.style.padding = "0";

    // Apply styles to personal info and residence info sections
    document.querySelectorAll(".personal-info-content, .residence-info-content, .foreigner-residence-content").forEach(section => {
        section.style.display = "grid";
        section.style.gridTemplateColumns = "repeat(2, 1fr)";
        section.style.gap = "20px";
        section.style.placeItems = "left";
        section.style.margin="0 15% 0 15%";
        
    });

    // Apply styles to form field containers
    document.querySelectorAll(".personal-info-content .mb-3, .residence-info-content .mb-3").forEach(field => {
        field.style.flex = "1 1 35%";
        field.style.maxWidth = "350px";
    });

    // Handle foreign location field visibility
    const foreignerCheckbox = document.querySelector("#id_is_foreigner");
    const foreignLocationField = document.querySelector("#foreignLocationField");
    const localLocationFields = document.querySelector("#localLocationFields");

    function toggleLocationFields() {
        if (foreignerCheckbox.checked) {
            foreignLocationField.classList.remove("hidden");
            localLocationFields.classList.add("hidden");
        } else {
            foreignLocationField.classList.add("hidden");
            localLocationFields.classList.remove("hidden");
        }
    }

    if (foreignerCheckbox) {
        // Initialize visibility based on the current state
        toggleLocationFields();

        // Add event listener to update visibility on change
        foreignerCheckbox.addEventListener("change", toggleLocationFields);
    }
});
