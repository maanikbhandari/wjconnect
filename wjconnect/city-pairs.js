// ID of the City Pairs div
var divId = 's-city-pairs';

// Select the div by its ID
var containerDiv = document.getElementById(divId);

// Check if the div exists
if (containerDiv) {
    // Select all divs with the specified class within the 's-city-pairs' div
    var divsWithClass = containerDiv.querySelectorAll('.virtual-choice-active');

    // Loop through each div with the class
    divsWithClass.forEach(function(activeDiv) {
        // Select all checkboxes within the active div
        var checkboxes = activeDiv.querySelectorAll('input[type="checkbox"]');

        // Loop through each checkbox
        checkboxes.forEach(function(checkbox) {
            // Do something with each checkbox (optional)
            // For example, check the checkbox
            checkbox.checked = true;
        });
    });
} else {
    console.error('Div with ID ' + divId + ' not found.');
}
