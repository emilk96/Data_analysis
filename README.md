# Data Analyser Berkules

This system can be used to find statistical information about given distance.txt files
and also be used to transform a large number of distance.txt files to the shortened 
`.csv` format 

There are two main scripts. The script `data_analyser.py` is used to find the lettering switch thresholds. These are saved in the `threshholds.json` file.
The script `cgom_to_kmer_v2.py` is used to transform the `txt_files/*.txt` files to the shortened `.csv` files using the information in the `thresholds.json` file.
The resulting files are saved at `csv_files/consolidated_data.csv`.

To use:

1. Place `.txt` files into the folder `txt_files`

2. Run to extract information and save to `.json` file.
```
python3 data_analyser.py
```

3. Run to transform all `.txt` files to `.csv`
```
python3 cgom_to_kmer_v2.py
``` 

