import pandas as pd
from pathlib import Path
import mpu.io

#Load thresholds from .json
thresholds = mpu.io.read('thresholds.json')

#Get all files in folder
p = Path('txt_files')
filenames = [i.stem for i in p.glob('**/*.txt')]
no_of_dataframes = len(filenames)

# Extraction code
data_total = [] #All of the relevant data from all files goes here  
for j, filename in enumerate(filenames):
    globals()['df_raw%s' % j] = pd.read_csv("txt_files/" + filename + ".txt", sep='\t')
    globals()['df_raw%s' % j].dropna(axis=1, inplace=True)

    # #Rename items in the column
    globals()['df_raw%s' % j]["label"].replace({'BG': 'W', 'Cap': 'A', 'Gauge': 'B', 'Pen': 'C', 'Pad': 'D', 'Tip': 'E', 'App': 'F'}, inplace=True) #Insert other renamings here
    
    # Add duration column
    globals()['df_raw%s' % j]['duration'] = globals()['df_raw%s' % j].apply(lambda x: x['end_time'] - x['start_time'], axis=1)

    # Replace if not in between threshold bounds (BG never gets replaced)
    # A -> K
    globals()['df_raw%s' % j].loc[(globals()['df_raw%s' % j]["duration"] >= thresholds[1][0]) & (globals()['df_raw%s' % j]["duration"] <= thresholds[1][1]) & (globals()['df_raw%s' % j]["label"] == "A" ), "label"] = "K"
    # B -> L
    globals()['df_raw%s' % j].loc[(globals()['df_raw%s' % j]["duration"] >= thresholds[2][0]) & (globals()['df_raw%s' % j]["duration"] <= thresholds[2][1]) & (globals()['df_raw%s' % j]["label"] == "B" ), "label"] = "L"
    # C -> M
    globals()['df_raw%s' % j].loc[(globals()['df_raw%s' % j]["duration"] >= thresholds[3][0]) & (globals()['df_raw%s' % j]["duration"] <= thresholds[3][1]) & (globals()['df_raw%s' % j]["label"] == "C" ), "label"] = "M"
    # D -> N
    globals()['df_raw%s' % j].loc[(globals()['df_raw%s' % j]["duration"] >= thresholds[4][0]) & (globals()['df_raw%s' % j]["duration"] <= thresholds[4][1]) & (globals()['df_raw%s' % j]["label"] == "D" ), "label"] = "N"
    # E -> O
    globals()['df_raw%s' % j].loc[(globals()['df_raw%s' % j]["duration"] >= thresholds[5][0]) & (globals()['df_raw%s' % j]["duration"] <= thresholds[5][1]) & (globals()['df_raw%s' % j]["label"] == "E" ), "label"] = "O"
    # F -> P
    globals()['df_raw%s' % j].loc[(globals()['df_raw%s' % j]["duration"] >= thresholds[6][0]) & (globals()['df_raw%s' % j]["duration"] <= thresholds[6][1]) & (globals()['df_raw%s' % j]["label"] == "F" ), "label"] = "P"

    #Select label column
    globals()['df_raw%s' % j] =  globals()['df_raw%s' % j][["label"]]

    #Write data to a string
    x = ""
    for i in range(len(globals()['df_raw%s' % j])):
        x = x + str( globals()['df_raw%s' % j]["label"].iloc[i])

    data_writer  = ['T'+str(j+1), x]
    data_total.append(data_writer)

#Make new dataframe that fits the format
df_out = pd.DataFrame(data_total, columns = ['Expert', 'UniColor'])

#Convert back to csv
df_out.to_csv("csv_files/" + "consolidated_data" + ".csv", index=False)


