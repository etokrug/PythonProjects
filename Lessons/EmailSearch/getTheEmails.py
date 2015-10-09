from glob import glob
import os
import shutil

FILESPEC = "C:/PythonData\*.eml"
files = glob(FILESPEC)
newDir = "./emailgrab/"

if not os.path.exists(newDir):
    os.makedirs(newDir)

for f in files:
    print(f)
    shutil.copy(f, "%s%s" % (newDir,f))
    