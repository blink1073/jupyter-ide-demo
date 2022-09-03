import json
import glob
import os
import os.path as osp

here = osp.dirname(osp.abspath(__file__))

def select_xpython(fname):
    with open(fname) as fid:
        data = json.load(fid)
    kernelspec = data['metadata']['kernelspec']
    kernelspec['name'] = kernelspec['display_name'] = 'xpython'

    with open(fname, 'w') as fid:
        json.dump(data, fid)

for fname in glob.glob(osp.join(here, os.pardir, '*.ipynb')):
    select_xpython(fname)
