# Virtual Linac
**This package is a research tool for my PhD dissertation at University of Toledo Medical Physics program.**
***
[![language](https://img.shields.io/badge/Python-3.8-brightgreen.svg?style=flat-square)](https://github.com/KanruXie/Virtual_Linac)
[![MC](https://img.shields.io/badge/MonteCarlo-MCNP5-blue.svg?style=flat-square)](https://github.com/KanruXie/Virtual_Linac)
***
## Description
*I'm still learning how to write a README file...*

The purpose of this software package is to conveniently create and use a Monte Carlo medical Linac
in MCNP5, including input file creating, output file analyzing, new beam and collimator
commissioning. GUI is designed for it's considered to be more friendly for this project.

Kind of a benchmarking product is the BEAMnrc of EGSnrc.
***
## Basic Structure
Following is a basic structure of the software package, for details please see Developer 
Manual in Documentations
* MAIN
  * main_window GUI
    
  * Global functions
    
  * Input file creator
    * Input window GUI
    * write cell card
    * write surface card
    * write material card
    * other functions
    
  * Output file analyzer
    * Output window GUI
    * read output file
    * analyze and create new file
    * Measure data folders
    
  * Beam commissioning
    * commissioning window GUI
    * spectrum
    * angular distribution
    * spatial distribution
    * combine new beam
    * Commissioned beam folder
    
  * Collimator designing
    * *Under Construction*
* GIT FILES
***
## Documentation
* Version Log
* User Manual
* Developer Manual
***
## A Brief History
* Started studying virtual Linac in late 2018, spend quite a long time to construct the full geometry of HD-MLC and 
commission the first beam,  Edge 6FFF. During this time two major issues were realized: 1) high frequency of making 
  mistakes when writing an input file; 2) tediousness of the repeating work to analyze output files. 
  
* Early 2020, campus shut down due to Covid-19 pandemic. Started learning Python when locked at home. A series of 
scripts were coded initially to help me do the virtual Linac study.
  
* Late 2020, personal study of Python reached the chapter of GUI. Created GUI for each function,
 then packed everything up into one.
  
* Early 2021, learned how to use GitHub for version control and project management. 

***
## Author & Maintainer
@KanruXie: kanru.xie@yahoo.com
@UToledoVLinac:UToledo.VLinac@gmail.com
***
## License
Apache 2.0

For University of Toledo Medical Physics research only.

