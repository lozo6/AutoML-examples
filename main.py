import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML

df_sparcs = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/autoML/datasets/data_sparcs.csv')

df_sparcs.columns
# Index(['Health Service Area', 'Hospital County',
#        'Operating Certificate Number', 'Facility Id', 'Facility Name',
#        'Age Group', 'Zip Code - 3 digits', 'Gender', 'Race', 'Ethnicity',
#        'Length of Stay', 'Type of Admission', 'Patient Disposition',
#        'Discharge Year', 'CCS Diagnosis Code', 'CCS Diagnosis Description',
#        'CCS Procedure Code', 'CCS Procedure Description', 'APR DRG Code',
#        'APR DRG Description', 'APR MDC Code', 'APR MDC Description',
#        'APR Severity of Illness Code', 'APR Severity of Illness Description',
#        'APR Risk of Mortality', 'APR Medical Surgical Description',
#        'Payment Typology 1', 'Payment Typology 2', 'Payment Typology 3',
#        'Birth Weight', 'Abortion Edit Indicator',
#        'Emergency Department Indicator', 'Total Charges', 'Total Costs'],
#       dtype='object')
