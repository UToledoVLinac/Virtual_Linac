# Version records for previous scripts before GUI assembled
## Version 0.1
  Basic Edge 6FFF Jaws model.
  
  Jaws positions are symmetrical, defined by trcl function.
  
  Four different objectives: x-, y-, z- lattice, and a W1 detector.
  
  Need to do in this version:
  
	1) Make the Jaws position asymmetrical, any position separately.
	2) Give warning if typed-in information is out of range or has fault.
	3) Make the objective volumes at any position in water tank.
	4) Check the line length, no more than 80 characters.
	5) Change directory and check if the input file name exists.  

## Version 0.2.0
  Added function 'line length check'

## Version 0.2.1
  Fixed typo in 'def jaws()': incorrect jaw cell number.
  Changed some words.
  Changed the variables 'depth' and 'lat_size' from in-def global to actual global.

## Version 0.3.0
  Jaws can be at any position asymmetrically now.

## Version 0.4.0
  Check if objective is acceptable (only x, y, z or d).
  
  Check if depth and lat_size is number only and in range.

## Version 0.5.0
  Check Jaws positions are number only and in range.
  
  Check X Jaws and Y Jaws collision.

## Version 0.5.1
Surface card, moved the Jaws surfaces into separate def module, more readable. 
***
## Version 1.0
  Edge 6FFF Jaws + MLCs
  
  Air_banks, mlc_surface, mlc_cell and trcl_mlc have separate test file.
  
  Need to do:
  
	1) MLC can move to symmetrical field opening.
	2) MLC can move to asymmetrical field opening.
	3) MLC can move by each blades separately to any position.
	4) Incorrect input check and MLC collision check.
	5) Think about easier expression for MLC cell and surface cards.

## Version 1.1.0
  Now MLCs can open symmetrically.
  
  Check if open field is number only and in range.
  
  Added function mlc_opening, to decide which leaf need to move.

## Version 1.1.1
  Solved issue: Outboard leaves trcl card line too long.
  
  MLC bank2 move in wrong direction fixed.
  
  Each MLC bank should move half of the x- field opening, fixed.
  
  Condition for Outboard leaves to move should be y- field less than 21 cm, fixed.
  
  Modified some format (not important).

## Version 1.1.2
  Added a lot of comments.
  
  Made some insignificant format changes.

## Version 1.2.0
  Added function check tally input.

## Version 1.2.1
  Deleted some unexpected spaces in 'imp:p,e 1' statements.
  
  In card had two 'qt2', corrected the first one to 'qt1'.
  
  Cell of water tank had one surface missing, added '-1'.

## Version 1.3.0
  Now able to return the current directory, choose a different path and create it if not exists.
  
  Check if the input file name already exists, and ask if you want to overwrite.

## Version 1.3.1
  Upgraded checking if file exists in current_directory, by using os.chdir.
  
  Corrected in len_check should open 'file_path', not 'title'.

## Version 1.4.0
  Rewrote objectives' surface and tally cards. 

## Version 1.5.0
  Serious error found. Water material card corrected.
  
  Spectrum will be changed, back to psf currently.
***
## Version 2.0.0
  GUI designed.
  
  Jaws only for this version. Functions are the same as previous programs.

## Version 2.1.0
  Added function x- and y- off axises, 0 by default.
  
  Rewrote surface card for x- and y- axises.
  
  Added content check for x- and y- axises.
  
  Added content check for nps and randseed if not blank.
  
  Renamed several variables.

## Version 2.2.0
  Added function and associated checking for cut off energies.
***
## Version 3.0.0
  GUI for both Jaws and MLC.
  
  Added functions of widgets layout and content check for MLC.
  
  Main algorithm for MLC was surprisingly easy to be moved from version 1.4.0, just renamed several variables, and put them in correct places. 
  
  Need to do:
  
	1) Different tallies.
	2) Customize MLC positions.
	3) Able to make a 2-D dose distribution. 

## Version 3.0.1
  Fixed issue: cell 2 missing a surface -1, causing particles lost. (AGAIN!!)

## Version 3.0.2
  Fixed x2 and y2 jaws in trcl* card need a negative sign to indicate opposite direction.

## Version 3.1.0
  Serious error found. Water material card corrected
  
  Now using angular dependent spectrum
  
  Added source spatial distribution
  
  trcl of Jaws calculation mistake corrected.

## Version 3.1.1
  Redesign layout
  
  Add MLC disable checkbox
  
  Add base plate

## Version 3.2.0
  MLC disable checkbox functioned: surface, cell, air_card, content_check
  
  Minor corrections
  
## Version 3.2.1
  Add comment box

## Version 3.2.2
  Corrected Jaws collision check (from + to -)

## Version 3.3.0
  Add directory change pop-up window
