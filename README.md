
Corresponding author: Michael Martini ([Mail](mailto:michael.martini1@rwth-aachen.de?subject=github-infix-mining))
and Daniel Schuster ([Mail](mailto:daniel.schuster@fit.fraunhofer.de?subject=github-infix-mining))


### Repository Structure
* The proposed Valid Tree Miner algorithms and the baseline Freqt algorithm are implemented in 
`Scripts/Algos/asai_performance.py` and `Scripts/Algos/valid_performance.py`.
* In `Scripts/run_eval.py` is a script to run the conducted experiments.

### Event Logs
To run the experiments real-world event logs in .XES format are needed. We provide the *Sepsis Cases* and *BPI 2020 (Prepaid_Travel_Cost)* event logs in this repository in the folder `Experiments/Datasets`. 
Please download the larger [BPI Challenge 2012](https://data.4tu.nl/articles/dataset/BPI_Challenge_2012/12689204) and [BPI Challenge 2017](https://data.4tu.nl/articles/dataset/BPI_Challenge_2017/12696884) event log seperatly and add them to the directory `Experiments/Datasets`, if you want to run the experiment with them. 

### Setup
* A requierments file for the virtual enviroment used to run the experiment is located in `Experiments/requirements.txt`
To run the setup you need to have [Python Version >=3.8.0](https://www.python.org/downloads/release/python-380/) and python virtualenv installed.   
  1. **Setup a clean virtualenv:** *python -m venv venv*
  2. **Install requierments:** *"./venv/Scripts/pip" install -r requirements.txt*
  3. **Activate the virtual enviorment:** *"./venv/Scripts/activate"*  

* A requierments file for the plotting [Jupyter Notebook](https://jupyter.org/) is located in `Plotting/requirements.txt`
  Open the notebook `Plotting/Plotting.ipynb` and run the first cell to install the packages via pip. 

### Experiments
After setting up the virtual enviroment for `Experiments/requirements.txt`, you can run the *experiments* by running `Experiments/run_eval.py` using Python, i.e., in `Experiments` after activating the virtual enviroment run *python run_eval.py*. The paths to the event logs, the event logs to consider and were to write the result, as well as parameters for the experiments can be edited in the `Experiments/run_eval.py`.
It will write the resulting experiment data from the runtime experiment `Experiments/Experiment_Scripts/test_performance.py` and `Experiments/Experiment_Scripts/test_memory.py` into the folder `Eval-Runs`. The reference results running the experiments are already present in the folder `Eval-Runs`.

The Experiments compare the implementation of the Valid Tree Miner `Experiments/Algos/valid_miner.py` against the implementation of the Freqt algorithm `Experiments/Algos/asai.py`

### Further Results
Plots on Runtime and Memory evaluation for the four considered real-world event logs (Sepsis, BPI 2012, BPI 2017, BPI 2020) and differnt support counting strategies are provided in the folder `Plotting/Figures`. 
