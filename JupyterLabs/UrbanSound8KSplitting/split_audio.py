import pandas as pd
import os

from collections import defaultdict
import shutil

# From https://serv.cusp.nyu.edu/projects/urbansounddataset/urbansound8k.html
urban_df = pd.read_csv('UrbanSound8K.csv')

# init dict's
reference_hash = defaultdict(str)
df_to_csv_split_hash = defaultdict(pd.DataFrame)

# preperations to split audio
for index, row in urban_df.iterrows():
    # separates foreground and background sounds int separate directories
    directory = ('foreground' if row['salience'] == 1 else 'background') + '_' + row['class']

    # class of the sound type
    class_name = row['slice_file_name']

    # used when moving files from original location to split location
    if not file_name in reference_hash:
        reference_hash[class_name] = directory

    # create the new direcotries if they don't exist
    if not os.path.exists('./audio/split_audio/' + directory):
        os.makedirs('./audio/split_audio/' + directory)

    # add row to hashed dataframe
    df_to_csv_split_hash[directory] = pd.concat([df_to_csv_split_hash[directory], row.to_frame().T])

# save data frame as csv for each category
for k in df_to_csv_split_hash:
    df_to_csv_split_hash[k].to_csv(path_or_buf='./audio/split_audio/' + k + '/' + k + '.csv')

# init direcotry traversing
src = './audio'
src_files = os.listdir(src)

# traverse original audio file direcotry and copy over to new split direcotires
for subdir, dirs, files in os.walk(src):

    if not 'split_audio' in subdir:
        print('processing: \t', subdir, '\n')
        for file in files:
            full_file_name = os.path.join(subdir, file)
            if full_file_name.endswith('.wav') and not subdir == './audio/split_audio/' + reference_hash[file]:
                shutil.copy(full_file_name, './audio/split_audio/' + reference_hash[file])