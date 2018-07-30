# TODO:

* Finish Adding details for README
* Add Config for screen dimensions (`800 x 480`? or something else?)
* Add "go back" button to stage 5
* Give more length to all labels, to accommodate for the new font
* make the UI in stage 5 more simple/tell them clearly what's going on
* Add tests for `PrinterUI` to ensure that it sets the stages correctly
* Add custom theme support!
* Write tests for BackendStatics
* Consider breaking BackendStatics into smaller parts
  * Put all higher level GUI Functions into a class for GUI Functions instead?
    * This class would inherit BackendStatics and be present in the GUI package instead
  * Put all the save functions into smaller parts too?
    * this would be better for testing

<hr>

### Completed

* Force Dialog to be in the center/top left corner
* **Bug report #001** - enter an incorrect student ID - can erase the error message! The other keys give silent errors also
    * **Fix**: Added Additional Checks to make sure that this issue cannot be raised again
      * **Cause**: At the time of creating `_isRemoveDigit`, I assumed that checking if it was equal to `DEFAULT_TEXT_lbl_St2_StudentIDDisplay` would be enough, need to consider it again
