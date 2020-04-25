import json
import os
import os.path as osp

here = osp.join(osp.abspath(__file__))

fname = osp.abspath(osp.join(here, '..', 'examples', 'Python.ipynb'))

with open(fname) as fid:
    data = json.load(fid)

data['metadata'] = {
  "kernelspec": {
   "display_name": "xpython",
   "language": "python",
   "name": "xpython"
  },
  "language_info": {
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "version": "3.7.3"
  }
 }

 with open(fname, 'w') as fid:
     json.dump(fid, data)
