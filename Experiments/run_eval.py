from Experiment_Scripts.test_memory import compare_occurence_list_size
from Experiment_Scripts.test_performance import compare_performance
from cortado_core.subprocess_discovery.subtree_mining.obj import (
    FrequencyCountingStrategy,
)

if __name__ == "__main__":

    files = [
        "Sepsis Cases",
        "BPI_CH_2020_PrepaidTravelCost",
        "BPI_Challenge_2012",
        "BPI Challenge 2017",
    ]

    output_path = "..//Eval-Runs//"
    log_path = "Datasets//"

    for file in files:

        log = log_path + file + ".xes"

        log_name = file
        timeout = 300  # 300 Second Timeout

        for strat, strat_name in [
            (FrequencyCountingStrategy.TraceTransaction, "TraceTransaction"),
            (FrequencyCountingStrategy.TraceOccurence, "TraceOccurence"),
            (FrequencyCountingStrategy.VariantOccurence, "VariantOccurence"),
            (FrequencyCountingStrategy.VariantTransaction, "VariantTransaction"),
        ]:
            #compare_performance(
            #    log, log_name, strat, strat_name, output_path, timeout, False
            #)
            compare_occurence_list_size(
                log, log_name, strat, strat_name, output_path, timeout, False
            )
