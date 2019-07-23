# this script convert the full dataset mitdb (data and annotatiosn) to text files

from os import listdir, makedirs, system, getcwd
from os.path import isfile, isdir, join, exists
import wfdb

#dir = 'ediagnostic/wfdb/'#'mitdb/'
# dir = getcwd() + '/database/mitdb/'
dir = 'database/mitdb/'
#Create folder

dir_out = dir + 'csv/'
if not exists(dir_out):
        makedirs(dir_out)
        wfdb.dl_database('mitdb', getcwd() + '/database/mitdb/', overwrite=True)

records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.dat') != -1)]
#print records

for r in records:

	command = 'rdsamp -r ' + dir + r[:-4] + ' -c -H -f 0 -v >' + dir_out + r[:-4] + '.csv'
	print(command)
	system(command)

	command_annotations = 'rdann -r ' + dir + r[:-4] +' -f 0 -a atr -v >' + dir_out + r[:-4] + '.ann'
	print(command_annotations)
	system(command_annotations)
