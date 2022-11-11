# AutoML-examples
HHA 507 Assignment 9

1. Create a new github repo called 'AutoML examples'

2. Select a dataset of your own choosing (or select my modified version of SPARCS - https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/autoML/datasets/data_sparcs.csv)

3. Create two 'experiments' using the autoML package mljar-supervised
One that is focused around classification (binary or multi-class outcome variable)
One that is focused around regression (continuous outcome variable)
4. Include the output of the mljar-supervised output folder inside of the github repo (e.g., so there should be 2 folders - one for classification and one for regression)

5. In a markdown file (readme.md):
    - Describe the two dependent variables (outcomes) for experiment 1 and experiment 2
    - Describe for each experiment:
        - What was the best performing model (please interpret (a) log-loss or RMSE between models, and (b) AUC)
        - How much better (? if any) did the model perform compared to baseline


# Project 1 (binary/classification)

The independent vairable tested was `Length of Stay`

The best performing model was XgBoost with a logloss of `0.800021` compared to Baseline logloss of `0.687821`

details in df_sparcs_binary_los


# Project 2:

The independent vairable tested was `Total Costs`

The best performng model was Ensemble with an RMSE of `6451.44` compared to Baseline RMSE of `23541.3`

details in AutoML_1
