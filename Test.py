import os
from shutil import copy
if os.path.exists('G:/CAFE_MONITOR/token.pickle') and os.path.getsize('G:/CAFE_MONITOR/token.pickle') == 0:
    print("Token.Pickle is Found with Zero byte.. Copying the backup...")
    copy('G:/CAFE_MONITOR/token_backup/token.pickle', 'G:/CAFE_MONITOR/')