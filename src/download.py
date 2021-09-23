import os
import tarfile
from time import time
import glob
import gdown

folders = {
           1999: '1ObZwt6cb97XogQoKu5vQvcnOzeQX4h_5',
           2001: '1ishYRAffV0pdos8wufxQwC4y00b89sd4',
           # 2002: '1_yoN_uqIcPv976jTJ3Aqyk1nuOPOaAvP',
           2004: '1bnRoWv3jtXTJrd1waVsqiWd-1k24XtyB',
           2005: '1g9Ap2i-yVqia1SQ0R4pAmdB_jvRBqogj',
           2007: '1eScmenYHUFvPxL_fe1UmT_QiK8M_VZ6c',
           2008: '1eScmenYHUFvPxL_fe1UmT_QiK8M_VZ6c',
           # 2009: '1ov0hQ3uDlg63K-zIbisE58QYyYgMtzOJ',
           # 2010: '1b6qydpGDjSuLcA5E_E2gQi2zQYmrzeNn',
           # 2011: '1R1I03oyEhk8WaAWhnYNsfsR9gDmfVugL',
           # 2013: '1se8x4MWy-dbK5UrPvNoRmRELAK8n0C6r',
           # 2014: '1HyY0PAzzlTG2ciy_zKJ1MOgsNIeNvLWi',
           # 2015: '1Ou2jROi2gwXkknQChtjNWn35dVktxIBC'
}


if not os.path.exists('dataset'):
    os.mkdir('dataset')

# Download the tar files
for YEAR in folders.keys():
    print("Downloading year ", YEAR)
    output = f'dataset/{YEAR}.tar'
    url = "https://drive.google.com/uc?id={id}".format(id=folders[YEAR])
    gdown.download(url, output, quiet=False)


# Extract the tar files
for f in glob.glob('dataset/*.tar'):
    t1 = time()
    with tarfile.open(f'{f}.tar', 'r') as fh:
        fh.extractall()
    print(f"Extracted {f}.tar in {time()-t1} s")
