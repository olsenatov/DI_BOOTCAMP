// Create an input type text that takes/shows only letters. (ie. numbers and special characters won’t be accepted)

// Hint: use one of the following events to remove any character that is not a letter

// keyup event
// or keypress event
// or keydown event
// or input event

// Hint : Check out keycodes in Javascript or Regular Expressions

document.getElementById('letterInput').addEventListener('input', function(event) {
    let inputValue = event.target.value;
    let formattedValue = inputValue.replace(/[^A-Za-z]/g, '');
    event.target.value = formattedValue;
  });

  //so input event it doesn't give you an option to input any other character at all