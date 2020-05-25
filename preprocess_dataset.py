import pandas as pd
import glob
import os

# get data files
path = r"/home/tdelatte/projects/eu-generator/data/datasets/EURLEX57K/"
folders = glob.glob(path + "**/*.json", recursive=True)

data = pd.concat((pd.read_json(file, lines=True) for file in folders), ignore_index=True)
small_data = data.drop(["celex_id", "uri", "type", "concepts", "header", "recitals", "attachments"], axis=1)
small_data["main_body"] = [" ".join(map(str, l)) for l in small_data["main_body"]]
# save to text file
# line_terminator uses tags to help ...
small_data.to_csv("data/eu_data.txt", index=False, sep=" ", header=None, line_terminator="<endoftext> \n <startoftext>")