#!/usr/bin/env python

"""
run_SVM.py
    
VARPA, University of Coruna
Mondejar Guerra, Victor M.
27 Oct 2017
"""

from train_SVM import *

# Call different configurations for train_SVM.py 

####################################################################################
winL = 90
winR = 90
do_preprocess = True
use_weight_class = True
maxRR = True
compute_morph = {''} # 'wvlt', 'HOS', 'myMorph'

multi_mode = 'ovo'
voting_strategy = 'ovo_voting'  # 'ovo_voting_exp', 'ovo_voting_both'

use_RR = False
norm_RR = False

oversamp_method = ''
feature_selection = ''
do_cross_val = ''
C_value = 0.001
reduced_DS = False # To select only patients in common with MLII and V1
leads_flag = [1,0] # MLII, V1

pca_k = 0

################

# With feature selection
ov_methods = {''}#, 'SMOTE_regular'}

C_values = {0.001, 0.01, 0.1, 1, 10, 100}
gamma_values = {0.0}
gamma_value = 0.0

conf_options = ('u-lbp', 'wvlt', 'HOS', 'myMorph', 'RR')

conf_list = []

for i in range(5):
    if(i<4):
        temp_conf = [set([conf_options[i]]), False, False]
    else:
        temp_conf = [set(['']), True, True]
    # conf.append(temp_conf.copy())
    for j in range(i,5):
        if i != j and j<4:
            temp_conf[0] = temp_conf[0].copy()
            temp_conf[0].add(conf_options[j])
        elif j == 4:
            temp_conf[1] = True
            temp_conf[2] = True
        conf.append(temp_conf.copy())


for conf in conf_list:
    for C_value in C_values:
        pca_k = 0

        use_RR = conf[1]
        norm_RR = conf[2]
        compute_morph = conf[0]
        main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)


    """

    # Single
    use_RR = False
    norm_RR = False
    compute_morph = {'u-lbp'}
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)


    use_RR = False
    norm_RR = False
    compute_morph = {'wvlt'}
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)


    use_RR = False
    norm_RR = False
    compute_morph = {'HOS'}
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)


    use_RR = False
    norm_RR = False
    compute_morph = {'myMorph'}
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)


    use_RR = True
    norm_RR = True
    compute_morph = {''}
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)

    
    # Two
    use_RR = True
    norm_RR = True
    compute_morph = {'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
    use_RR = False
    norm_RR = False

    compute_morph = {'wvlt', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
            
    compute_morph = {'HOS', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)

    compute_morph = {'myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
             


    # Three
    use_RR = True
    norm_RR = True
    compute_morph = {'wvlt', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
            
    compute_morph = {'HOS', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)

    compute_morph = {'myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
     
    use_RR = False
    norm_RR = False
    compute_morph = {'wvlt','HOS', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
            
    compute_morph = {'wvlt','myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
     

    compute_morph = {'HOS','myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
     


    # four
    use_RR = True
    norm_RR = True
    compute_morph = {'wvlt', 'HOS', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)

    compute_morph = {'wvlt', 'myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
     

    compute_morph = {'HOS','myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
     
    use_RR = False
    norm_RR = False
    compute_morph = {'wvlt', 'HOS','myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
     

    
    # five
    use_RR = True
    norm_RR = True
    compute_morph = {'wvlt', 'HOS','myMorph', 'u-lbp'} 
    main(multi_mode, 90, 90, do_preprocess, use_weight_class, maxRR, use_RR, norm_RR, compute_morph, oversamp_method, pca_k, feature_selection, do_cross_val, C_value, gamma_value, reduced_DS, leads_flag)
    """