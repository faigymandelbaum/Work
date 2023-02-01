import os
import sys


# Hardcoded folder names:
CURR_DIR = os.path.dirname(__file__)
sys.path.append(CURR_DIR)
INFO_FOLDER = CURR_DIR + '/info'
LOG_FOLDER =  CURR_DIR + '/logs'
HALLS_INFO_FILE = 'halls.csv'
FAMILIES_INFO_FILE = 'families.csv'
COLORS_INFO_FILE = 'colors.csv'
LOG_FILE = LOG_FOLDER + '/wedding_logs.txt'
