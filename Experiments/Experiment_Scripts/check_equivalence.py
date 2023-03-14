from typing import Set
from cortado_core.subprocess_discovery.subtree_mining.maximal_connected_components.maximal_connected_check import (
    check_if_valid_tree
) 

from cortado_core.subprocess_discovery.subtree_mining.tree_pattern import TreePattern


def check_equivalent(patterns_1 : dict[int, Set[TreePattern]], patterns_2 : dict[int, Set[TreePattern]], verbosity):
    
    # Check if the one set contains infix subtrees of a larger size and if so if there is any valid one missed by the algorithm
    if max(patterns_1.keys()) != max(patterns_2.keys()): 
        
        if max(patterns_1.keys()) > max(patterns_2.keys()):
            check_patterns = patterns_1
            high_key = max(list(patterns_1.keys()))
            low_key = max(list(patterns_2.keys()))
        else:  
            check_patterns = patterns_2
            low_key = max(list(patterns_1.keys()))
            high_key = max(list(patterns_2.keys()))
        
        
        for k in range(low_key + 1, high_key + 1): 
             if any([check_if_valid_tree(pattern.tree) for pattern in check_patterns[k]]):    
                print('Found valid subtree of size:', k)               
                return False
    
    for k in patterns_1.keys(): 
        
        vld_pattern1 = __get_maximal_patterns(patterns_1[k])
        cld_pattern1 = __get_closed_patterns(patterns_1[k])
        max_pattern1 = __get_maximal_patterns(patterns_1[k])
        
        vld_pattern2 = __get_maximal_patterns(patterns_2[k])
        cld_pattern2 = __get_closed_patterns(patterns_2[k])
        max_pattern2 = __get_maximal_patterns(patterns_2[k])
        
        if vld_pattern1 != vld_pattern2: 
            
            if verbosity > 0: 
                print('Mismatching Number of Valid Patterns:', len(vld_pattern1), len(vld_pattern2))   

            if verbosity > 1: 
                
                print('Valid Patterns only in Patterns 1:')
                for p in vld_pattern1.difference(vld_pattern2):
                    print(p)
                    
                print('Valid Patterns only in Patterns 2:')
                for p in vld_pattern2.difference(vld_pattern1):
                    print(p)
                    
            return False 
        
        elif verbosity > 2: 
            print('Number of Valid Patterns:', len(vld_pattern1))
        
        if cld_pattern1 != cld_pattern2: 
            
            if verbosity > 0: 
                print('Mismatching Number of Closed Patterns:', len(cld_pattern1), len(cld_pattern2))   
                
            if verbosity > 1: 
                
                print('Closed Patterns only in Patterns 1:')
                for p in cld_pattern1.difference(cld_pattern2):
                    print(p)
                    
                print('Closed Patterns only in Patterns 2:')
                for p in cld_pattern2.difference(cld_pattern1):
                    print(p)
                    
            return False 
        
        elif verbosity > 2: 
            print('Number of Closed Patterns:', len(cld_pattern1))
            
        if max_pattern1 != max_pattern2: 
            
            if verbosity > 0: 
                print('Mismatching Number of Maximal Patterns:', len(max_pattern1), len(max_pattern2))   
                
            if verbosity > 1: 
                
                print('Maximal Patterns only in Patterns 1:')
                for p in max_pattern1.difference(max_pattern2):
                    print(p)
                    
                print('Maximal Patterns only in Patterns 2:')
                for p in max_pattern2.difference(max_pattern1):
                    print(p)
                    
            return False 
        
        elif verbosity > 2: 
            print('Number of Maximal Patterns:', len(max_pattern1))
        
    return True 
    

def __get_closed_patterns(patterns : Set[TreePattern]): 
    return set([str(pattern) for pattern in patterns if pattern.closed and check_if_valid_tree(pattern.tree)])

def __get_maximal_patterns(patterns : Set[TreePattern]): 
    return set([str(pattern) for pattern in patterns if pattern.maximal and check_if_valid_tree(pattern.tree)])
    
def __get_maximal_patterns(patterns : Set[TreePattern]): 
    return set([str(pattern) for pattern in patterns if check_if_valid_tree(pattern.tree)])