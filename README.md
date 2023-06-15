
Corresponding author: Michael Martini ([Mail](mailto:michael.martini1@rwth-aachen.de?subject=github-infix-mining))
and Daniel Schuster ([Mail](mailto:daniel.schuster@fit.fraunhofer.de?subject=github-infix-mining))


### Repository Structure
* The proposed Valid Tree Miner algorithms and the baseline Freqt algorithm are implemented in 
`Experiments/Algos/freqt.py` and `Experiments/Algos/valid.py` using the code from the [cortado-core](https://github.com/fit-daniel-schuster/cortado-core) implementation used in [Cortado](https://cortado.fit.fraunhofer.de/). In `Experiments/run_eval.py` is a script to run the conducted experiments on Runtime and Memory Usage. 
* Result in form of .CSV files are written into the folder `Eval-Runs`. 
* The folder `Plotting` contains a Jupyter Notebook used for the creating of the plots in `Plotting/Figures` based on the results in `Eval-Runs`.

### Event Logs
To run the experiments real-world event logs in .XES format is needed. We provide the *Sepsis Cases* and *BPI 2020 (Prepaid_Travel_Cost)* event logs in this repository in the folder `Experiments/Datasets`. 
The larger [BPI Challenge 2012](https://data.4tu.nl/articles/dataset/BPI_Challenge_2012/12689204) and [BPI Challenge 2017](https://data.4tu.nl/articles/dataset/BPI_Challenge_2017/12696884) are compressed as a .ZIP and need to be decompressed first to get the .XES file

### Setup
* A requirements file for the virtual environment used to run the experiment is located in `Experiments/requirements.txt`
To run the setup you need to have [Python Version >=3.8.0](https://www.python.org/downloads/release/python-380/) and python virtualenv installed.   
  1. **Setup a clean virtualenv:** *python -m venv venv*
  2. **Install requirements:** *"./venv/Scripts/pip" install -r requirements.txt*
  3. **Activate the virtual environment:** *"./venv/Scripts/activate"*  

* A requirements file for the plotting [Jupyter Notebook](https://jupyter.org/) is located in `Plotting/requirements.txt`. 
  Setup a [Jupyter](https://jupyter.org/install) or [Jupyter Lab](https://jupyter.org/install) environment and start it. Open the notebook `Plotting/Plotting.ipynb` and run the first cell to install the packages via pip. 

### Experiments
After setting up the virtual environment for `Experiments/requirements.txt`, you can run the *experiments* by running `Experiments/run_eval.py` using Python, i.e., in `Experiments` after activating the virtual environment run the command *python run_eval.py*. The paths to the event logs, the event logs to consider, and were to write the result, as well as parameters for the experiments can be edited in the `Experiments/run_eval.py`.
It will write the resulting experiment data from the runtime experiment `Experiments/Experiment_Scripts/test_performance.py` and `Experiments/Experiment_Scripts/test_memory.py` into the folder `Eval-Runs`. The reference results running the experiments are already present in the folder `Eval-Runs`.

The Experiments compare the implementation of the **Valid Tree Miner** `Experiments/Algos/valid_miner.py` against the implementation of the **FREQT** algorithm `Experiments/Algos/freqt.py` in terms of runtime and memory usage.

### Further Results
Plots on **Runtime** and **Memory usage** for the four considered real-world event logs *(Sepsis, BPI 2012, BPI 2017, BPI 2020)* and different support counting strategies are provided in the folder `Plotting/Figures`. 
