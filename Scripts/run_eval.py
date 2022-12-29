from test_memory_occ_list_size import compare_occurence_list_size
from test_performance import compare_all
from cortado_core.subprocess_discovery.subtree_mining.obj import FrequencyCountingStrategy


if __name__ == "__main__":
    
    files = ['BPI_CH_2020_PrepaidTravelCost', 'Sepsis Cases - Event Log', "BPI_Challenge_2012", 'BPI Challenge 2017']

    for file in files:

        log_path = ""
        log = log_path + file + ".xes"
        
        log_name = file
        timeout = 300  # 300 Second Timeout
        
        for strat, strat_name in [
            (FrequencyCountingStrategy.TraceTransaction, "TraceTransaction"),
            (FrequencyCountingStrategy.TraceOccurence, "TraceOccurence"),
            (FrequencyCountingStrategy.VariantOccurence, "VariantOccurence"),
            (FrequencyCountingStrategy.VariantTransaction, "VariantTransaction"),
        ]:
            compare_all(log, log_name, strat, strat_name, timeout, False)
            compare_occurence_list_size(
                log, log_name, strat, strat_name, timeout, False
            )