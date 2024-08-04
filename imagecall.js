function theCommand(imageFile) {
    var commandInput = document.getElementById("commandInput");
    var command = commandInput.value;
  
    var image = document.getElementById("imgResult");
    image.src = imageFile;
  
    if (command == "greatguy") {
      command = "is not epic";
    } else if (command == "make rooster noise") {
      command = "COCK-A-DOODLE-DOO";
    } else if (command == "show duck image") {
      command == imageFile;
    } else if (command != "make duck noise" || command != "make rooster noise") {
      command = "Invalid command";
    }
  
    var commandSpan = document.getElementById("result");
    commandSpan.innerHTML = command;
  }