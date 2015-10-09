import glob
import os
import zipfile

def zarchive(fn, path):
    parent = os.path.split(path)[-1]
    #parent = os.path.basename(path)
    files = [true_file for true_file in glob.glob(os.path.join(path, "*")) if os.path.isfile(true_file)]
    zf = zipfile.ZipFile(fn, "w", zipfile.ZIP_DEFLATED)
    for fn_to_archive in files:
        child = os.path.basename(fn_to_archive)
        hero = os.path.join(parent, child)
        zf.write(fn_to_archive, hero)
    zf.close()
    return set(zf.namelist())