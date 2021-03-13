import pandas as pd
from pathlib import Path
import mpu.io

#Get all files in folder
p = Path('txt_files')
filepaths = [str(i) for i in p.glob('**/*.txt')]

#Make new dataframe
df = pd.DataFrame()

#Extract all the data
for i, filepath in enumerate(filepaths):
    tempdf = pd.read_csv(filepath, sep='\t')
    df = df.append(tempdf)

#Drop empty columns
df.dropna(axis=1, inplace=True)


#Create views (be careful with manipulating the underlying dataframe)
BG_duration_view = df[df['label'] == 'BG']['end_time']-df[df['label'] == 'BG']['start_time']
Cap_duration_view = df[df['label'] == 'Cap']['end_time']-df[df['label'] == 'Cap']['start_time']
Gauge_duration_view = df[df['label'] == 'Gauge']['end_time']-df[df['label'] == 'Gauge']['start_time']
Pen_duration_view = df[df['label'] == 'Pen']['end_time']-df[df['label'] == 'Pen']['start_time']
Pad_duration_view = df[df['label'] == 'Pad']['end_time']-df[df['label'] == 'Pad']['start_time']
Tip_duration_view = df[df['label'] == 'Tip']['end_time']-df[df['label'] == 'Tip']['start_time']
App_duration_view = df[df['label'] == 'App']['end_time']-df[df['label'] == 'App']['start_time']

# Example code to do data analysis
# find mean: BG_duration_view.mean()
# find standard deviation: BG_duration_view.std()
BG_m = BG_duration_view.mean()
BG_std = BG_duration_view.std()
Cap_m = Cap_duration_view.mean() 
Cap_std = Cap_duration_view.std() 
Gauge_m = Gauge_duration_view.mean()
Gauge_std = Gauge_duration_view.std()
Pen_m = Pen_duration_view.mean()
Pen_std = Pen_duration_view.std()
Pad_m = Pad_duration_view.mean()
Pad_std = Pad_duration_view.std()
Tip_m = Tip_duration_view.mean()
Tip_std = Tip_duration_view.std()
App_m = App_duration_view.mean()
App_std = App_duration_view.std()

# Threshhold is if in standard deviation from mean
BG_threshold = [BG_m - BG_std*0.5, BG_m + BG_std*0.5]
Cap_threshold = [Cap_m - Cap_std*0.5, Cap_m + Cap_std*0.5]
Gauge_threshold = [Gauge_m - Gauge_std*0.5, Gauge_m + Gauge_std*0.5]
Pen_threshold = [Pen_m - Pen_std*0.5, Pen_m + Pen_std*0.5]
Pad_threshold = [Pad_m - Pad_std*0.5, Pad_m + Pad_std*0.5]
Tip_threshold = [Tip_m - Tip_std*0.5, Tip_m + Tip_std*0.5]
App_threshold = [App_m - App_std*0.5, App_m + App_std*0.5]

# Put all of the threshold data into list and dump to .json for easy loading in other scipt
data = [
BG_threshold,
Cap_threshold,
Gauge_threshold,
Pen_threshold,
Pad_threshold,
Tip_threshold,
App_threshold]

mpu.io.write('thresholds.json', data)


