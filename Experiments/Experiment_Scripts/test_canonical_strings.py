
from pm4py.objects.log.importer.xes.importer import apply as xes_import
from cortado_core.utils.cvariants import get_concurrency_variants
from Algos.freqt import min_sub_mining_freqt
from Algos.valid import min_sub_mining_performance

from cortado_core.subprocess_discovery.subtree_mining.treebank import (
    create_treebank_from_cv_variants,
)

from cortado_core.subprocess_discovery.subtree_mining.maximal_connected_components.maximal_connected_check import set_maximaly_closed_patterns
from cortado_core.utils.timestamp_utils import TimeUnit

from cortado_core.subprocess_discovery.subtree_mining.obj import (
    FrequencyCountingStrategy,
)

from Experiment_Scripts.check_equivalence import check_equivalent
from Experiment_Scripts.exit_after import run_mining_eval

def compare_mining_results(
    log, log_name, strategy, strategy_name, timeout, artStart, verbosity
):

    print("Loading Log " +  log_name + " ...")
    log = xes_import(log)

    print("Creating Variants...")
    variants = get_concurrency_variants(log, False)

    print("Creating  Treebank...")
    treeBank = create_treebank_from_cv_variants(variants, artStart)
    
    min_sups = [0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0375, 0.025, 0.01]

    tTraces = sum([len(variants[variant]) for variant in variants])
    tTrees = len(variants)
    
    print("Mining Patterns using " + strategy_name)

    bailouted = {}
    
    for rel_sup in min_sups:

        if (
            strategy == FrequencyCountingStrategy.TraceOccurence
            or strategy == FrequencyCountingStrategy.TraceTransaction
        ):
            abs_sup = round(tTraces * rel_sup)
        else:
            abs_sup = round(tTrees * rel_sup)

        reps = 1 
        
        print()
        print("Current Sup Level:", rel_sup)
        print("Abs Sup", abs_sup)
        print()

        performanceTest = [
            (
                min_sub_mining_performance,
                {
                    "frequency_counting_strat": strategy,
                    "treebank": treeBank,
                    "k_it": 100,
                    "min_sup": abs_sup,
                    "bfs_traversal": True,
                },
                "Valid (BFS)",
            ),
            (
                min_sub_mining_freqt,
                {
                    "frequency_counting_strat": strategy,
                    "treebank": treeBank,
                    "k_it": 100,
                    "min_sup": abs_sup,
                    "no_pruning": True,
                },
                "NoPruning",
            ),
            (
                min_sub_mining_freqt,
                {
                    "frequency_counting_strat": strategy,
                    "treebank": treeBank,
                    "k_it": 100,
                    "min_sup": abs_sup,
                    "no_pruning": False,
                },
                "freqt",
            ),
        ]

        compare_dict = {}

        for algo, prms, name in performanceTest:
            
            if not name in bailouted:
                _, k_patterns, _, bailOut = run_mining_eval(
                    algo, timeout, prms=prms, repeats=reps
                )
                
            else:
                bailouted[name] = True
                bailOut = True
                
            if bailOut:
                bailouted[name] = True

            else: 
                
                set_maximaly_closed_patterns(k_patterns)
                compare_dict[name] = k_patterns

        compare_names = list(compare_dict.keys())
        
        if len(compare_names) > 1: 
            
            for name1, name2 in zip(compare_names, compare_names[1:]): 
            
                if verbosity > 0: 
                    print("Comparing", name1, "and", name2)
                
                if not check_equivalent(compare_dict[name1], compare_dict[name2], verbosity):
                    print('Found non-matching output for', log_name, name1, name2, rel_sup)
                    return False
                
    return True
                
        
                    
                
