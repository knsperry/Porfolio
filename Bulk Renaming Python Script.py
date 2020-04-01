import csv
import pandas as pds
import os
import glob
import time
import shutil

os.chdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output')

oldcsvfolder_output = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output\\Old CSV Sheets'

oldcsvfiles_output = glob.glob(os.path.join('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output','*.csv'))

for f in oldcsvfiles_output:
    shutil.move(f,oldcsvfolder_output)

os.chdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input')

mycsvdir = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input'

csvfiles = glob.glob(os.path.join(mycsvdir,'*.csv'))

dataframes = []
for csvfile in csvfiles:
    df=pds.read_csv(csvfile)
    dataframes.append(df)
    
combined_csv_files = pds.concat(dataframes, ignore_index = True)

combined_csv_files['Original Name'] = combined_csv_files.File_Path_and_Name.str[71:-4]

os.chdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output')

timestr = time.strftime("%m%d%Y-%H%M%S")

combined_csv_files.to_csv('Image Renaming Completed {}.csv'.format(timestr), index=False)

os.chdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input')


mocks1_list = os.listdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks1')
mocks2_list = os.listdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks2')
mocks3_list = os.listdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks3')
mocks4_list = os.listdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks4')
mocks5_list = os.listdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks5')

os.chdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output')

renamingfile = combined_csv_files

renamingfile = renamingfile.drop(columns='File_Path_and_Name')

renamingfile=renamingfile.set_index('Original Name')['New Name'].to_dict()

mocks1_path = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks1'
mocks2_path = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks2'
mocks3_path = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks3'
mocks4_path = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks4'
mocks5_path = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Mocks5'

mocks1_pathoutput = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output\\Mocks1'
mocks2_pathoutput = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output\\Mocks2'
mocks3_pathoutput = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output\\Mocks3'
mocks4_pathoutput = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output\\Mocks4'
mocks5_pathoutput = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Output\\Mocks5'

def rename(infile, outfile):
    
    for filename in os.listdir(infile):
        oldname = filename
        newname = str(renamingfile[os.path.splitext(filename)[0]]) + str(os.path.splitext(filename)[1])
        os.rename(os.path.join(infile,oldname), os.path.join(outfile, newname))

rename(mocks1_path, mocks1_pathoutput)
rename(mocks2_path, mocks2_pathoutput)
rename(mocks3_path, mocks3_pathoutput)
rename(mocks4_path, mocks4_pathoutput)
rename(mocks5_path, mocks5_pathoutput)

os.chdir('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input')

oldcsvfolder_input = 'M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input\\Old CSV Sheets'

oldcsvfiles_input = glob.glob(os.path.join('M:\\eCommerce\\Item Set Up Sheets (ISS)\\Bulk Image Renaming\\Input','*.csv'))

for f in oldcsvfiles_input:
    shutil.move(f,oldcsvfolder_input)