from datetime import date
from datetime import time
from datetime import datetime
import os

today = date.today()
date_time = datetime.now()
print(f"Today's date is: {today}")
print(f"All together now:{date_time} ")

dirpath = os.getcwd()
print("your current directory is : ", dirpath)
foldername = os.path.basename(dirpath)
print("The directory name is: ", foldername)

# file metadata
# st_mode - protection mode
# st_ino - inode number
# st_dev - device
# st_nlink - number of hard links
# st_uid - user id of owner
# st_getid - group id of owner
# st_size - size of files, in bytes
# st_atime - time of most recent access
# st_mtime - time of most recent content modification
# st_ctime - time of  most recent metadata change