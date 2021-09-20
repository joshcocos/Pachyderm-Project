import os
import csv
import glob
from datetime import datetime

# log_parser reads log files (*.log only) from /pfs/log_files/*
# and outputs a csv with the count of lines for both 'error' 
# and 'warning' for each log file.

start_time = datetime.now()
with open("/pfs/out/log_analysis_%s.csv" % str(start_time).replace(' ','T').replace(':','_'),'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    writer.writerow(['Filename','Warning Count','Error Count'])
    paths = glob.glob('/pfs/log_files/*.log')
    for path in paths:
        warning_count = 0
        error_count = 0
        open_file = open(path)
        for line in open_file:
            if 'warning' in line.lower():
                warning_count += 1
            if 'error' in line.lower():
                error_count += 1
        writer.writerow([path.split('/',3)[3],str(warning_count),str(error_count)])