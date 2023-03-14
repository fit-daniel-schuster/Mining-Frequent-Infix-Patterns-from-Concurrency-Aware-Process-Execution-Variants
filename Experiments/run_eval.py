from Experiment_Scripts.test_memory import compare_occurence_list_size
from Experiment_Scripts.test_performance import compare_performance
from cortado_core.subprocess_discovery.subtree_mining.obj import (
    FrequencyCountingStrategy,
)

from Experiment_Scripts.test_canonical_strings import compare_mining_results

import sys

if __name__ == "__main__":

    files = [
        "BPI_Challenge_2012",
        "BPI Challenge 2017",
        "PrepaidTravelCost",
        "Sepsis Cases",
    ]

    output_path = "..//Eval-Runs//"
    log_path = "Datasets//"

    for file in files:

        log = log_path + file + ".xes"

        log_name = file
        timeout = 300  # 300 Second Timeout

        for strat, strat_name in [
            (FrequencyCountingStrategy.TraceOccurence, "TraceOccurence"),
            (FrequencyCountingStrategy.VariantOccurence, "VariantOccurence"),
            (FrequencyCountingStrategy.VariantTransaction, "VariantTransaction"),
            (FrequencyCountingStrategy.TraceTransaction, "TraceTransaction"),
        ]:
            #compare_performance(
            #    log, log_name, strat, strat_name, output_path, timeout, False
            #)
            
            #compare_occurence_list_size(
            #    log, log_name, strat, strat_name, output_path, timeout, False
            #)
            
            
            if not compare_mining_results(log, log_name, strat, strat_name, timeout, False, 1): 
                sys.exit()