
Corresponding author: Michael Martini ([Mail](mailto:michael.martini1@rwth-aachen.de?subject=github-infix-mining))
Corresponding author: Daniel Schuster ([Mail](mailto:daniel.schuster@fit.fraunhofer.de?subject=github-infix-mining))


### Repository Structure
* The proposed Valid Tree Miner algorithms and the baseline Freqt algorithm are implemented in 
`Scripts/Algos/asai_performance.py` and `Scripts/Algos/valid_performance.py`.
* In `Scripts/run_eval.py` is a script to run the conducted experiments.

### Setup
* A requierments file for the virtual enviroment used to run the experiment is located in 'Scripts/requierments.txt'
To run the setup you need to have [Python Version >=3.8.0](https://www.python.org/downloads/release/python-380/) and python virtualenv installed.   
  1. Setup a clean virtualenv: python -m venv venv
  2. Install requierments: venv/Scripts/python pip install -r -requierments.txt
  3. Install cortado-core from github:  venv/Scripts/python pip install https://github.com/fit-daniel-schuster/cortado-core
  4. Open the enviorment: venv/Scripts/activate.bat 
 
Single line setup: 

python -m venv venv && venv/Scripts/python pip install -r -requierments.txt 



* A requierments file for the virtual enviorment used to run the plotting Jupyter Notebook is located in 'Plotting/requierments.txt'

### Experiments
*
*
*

### Further Results

This repository contains additional Figure and the orginal Eval-Runs. 
The results/plots are located in `Plotting/Figure` and the Eval-Runs in 'Plotting/Eval-Runs'.
