# VERSIONS NOTE
(Version control and management were not done very well since working on full GUI. It's very different now from previous scripts, why not re-number the versions from v1.0.0)
***
#### V1.1.2
MLC Bugs fixed:

* MLC QI surface card: surface 103 should be 'pz -50.98', surface 160 should be 'px -15'

* MLC x-movement should be 51/200 of fs, because of 51cm distance to source.

***
#### V1.1.1
* In y-profile analysis, fixed the problem with the repeated cell lettice at the 
center of the field
  
* Difference calculation of profiles re-written according to new format of measured data.
***
### V1.1.0
* Organized measured data better

* In beam commissioning, added uniform spatial distribution, no longer 
convert Gaussian sd and fwhm
***
#### V1.0.1
Fixed the calculation mistake in X Jaws trcl card, where we need to use fs / 100 but not / 200. This 
is a mistake associated with the issue of how to define the Jaws position from input window. 
Field size calculations were fixed but this one here was forgotten.
***
## V1.0.0
GUI designed and packed with:
1. Main window
2. Input File Create window (almost fully functioned)
3. Output File Analyze window (a lot to improve)
4. New Beam Commissioning (a lot to improve)
5. Collimator Designing window (not started yet)
6. Instruction Manual (document created)
