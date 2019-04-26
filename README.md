# ctypes vlfeat wrapper
This is a minimal wrapper for (some of) vlfeat 0.9.20 in Linux. It can be added on your PYTHONPATH without disrupting anything else.  It should work with any version of Python 2 or 3 that has numpy and ctypes.  
There is a more complete, conda/pip installable wrapper that mimics the matlab interface for vlfeat at https://github.com/menpo/cyvlfeat. 


# Use
1. In the repository root, run `python configure.py`
 
2. If vlfeat compiles successfully the script will produce another script called `set_paths.sh`.
```
source set_paths.sh
```
will set PYTHONPATH and LD_LIBRARY_PATH environmental variables.

3. Ready to use, simple example:
```
import matplotlib.pyplot as plt
import numpy as np
import vlfeat as vlf

im = plt.imread('someimage.jpg')
im_gray = np.mean(im, axis=2)
features = vlf.dsift(im_gray, 10, 20)
```
