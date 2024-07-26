import pandas as pd
#import numpy as np


column_names = ['id', 'xmin', 'xmax', 'ymin', 'ymax']


path = r'C:\Users\HP\Desktop\ranjanaa\kla\Dataset-0\Dataset-0\1st\CareAreas.csv'  # path to CareAreas.csv
path2 = r'C:\Users\HP\Desktop\ranjanaa\kla\Dataset-0\Dataset-0\1st\metadata.csv'  # path to metadata.csv


ca = pd.read_csv(path, names=column_names, header=None)
md = pd.read_csv(path2)


main_field_size = md['Main Field Size'][0]
sub_field_size = md['Sub Field size'][0]


mf = []
sf = []


mf_id = 0
for index, row in ca.iterrows():
    len_of_ca = row['xmax'] - row['xmin']
    br_of_ca = row['ymax'] - row['ymin']
    mf.append([
        mf_id,
        row['xmin'],
        row['xmin'] + main_field_size,
        row['ymin'],
        row['ymin'] + main_field_size
    ])
    mf_id += 1


mf_df = pd.DataFrame(mf, columns=['id', 'xmin', 'xmax', 'ymin', 'ymax'])
file_path = r'C:\Users\HP\Desktop\ranjanaa\kla\Dataset-0\Dataset-0\1st\mainfields.csv'
mf_df.to_csv(file_path, index=False, header=False)


sf_id = 0
for index, row in ca.iterrows():
    mfid, xmin, xmax, ymin, ymax = row
    x=xmin
    while x<xmax:
        y=ymin
        while y<ymax:
            sf.append([sf_id, x, x + sub_field_size, y, y + sub_field_size, mfid])
            sf_id += 1
            y+=sub_field_size
        x+=sub_field_size

    '''for x in np.arange(xmin, xmax, sub_field_size):
        for y in np.arange(ymin, ymax, sub_field_size):
            sf.append([sf_id, x, x + sub_field_size, y, y + sub_field_size, mfid])
            sf_id += 1'''


sf_df = pd.DataFrame(sf, columns=['sfid', 'xmin', 'xmax', 'ymin', 'ymax', 'mfid'])
file_path_sf = r'C:\Users\HP\Desktop\ranjanaa\kla\Dataset-0\Dataset-0\1st\subfields.csv'
sf_df.to_csv(file_path_sf, index=False, header=False)

print("Main fields and sub fields have been generated and saved to CSV files.")
