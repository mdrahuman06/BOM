console.log("BOM System JS Loaded.");

// Example of a simple interactive feature: toggle active class in navbar
document.addEventListener("DOMContentLoaded", () => {
    // Add event listeners for active links in the navbar
    const navLinks = document.querySelectorAll(".navbar a");
    navLinks.forEach(link => {
        link.addEventListener("click", function() {
            // Remove the active class from all links
            navLinks.forEach(link => link.parentElement.classList.remove("active"));
            // Add the active class to the clicked link
            this.parentElement.classList.add("active");
        });
    });
});

// Additional example: Log form submissions
const forms = document.querySelectorAll("form");
forms.forEach(form => {
    form.addEventListener("submit", () => {
        console.log("Form Submitted!");
    });
});

// For showing/hiding the "Other" field for item_type
function toggleCustomItemType() {
    const itemTypeSelect = document.getElementById('id_item_type');  // Accessing the item_type dropdown
    const customItemTypeDiv = document.getElementById('custom_item_type_div');  // The div for the custom input field
    
    // Check if 'Other' is selected in the dropdown
    if (itemTypeSelect.value === 'other') {
        customItemTypeDiv.style.display = 'block';  // Show the input field if "Other" is selected
    } else {
        customItemTypeDiv.style.display = 'none';  // Hide the input field otherwise
    }
}

// Initialize visibility based on the current selection
document.addEventListener('DOMContentLoaded', () => {
    toggleCustomItemType();  // Call to set the initial state when the page loads
});

// Add event listener to change visibility when the dropdown value changes
document.getElementById('id_item_type').addEventListener('change', toggleCustomItemType);
