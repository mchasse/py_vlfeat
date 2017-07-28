import os

os.chdir("vlfeat-0.9.20")
os.system("make")
os.chdir("../ctypes_wrapper")
os.system("make")
os.chdir("..")

this_dir = os.path.dirname(os.path.abspath(__file__))
ff=open("set_paths.sh","w")
ff.write("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:{}\n"
             .format(os.path.join(this_dir,"vlfeat-0.9.20/bin/glnxa64")))
ff.write("export PYTHONPATH=$PYTHONPATH:{}\n"
         .format(os.path.join(this_dir,'ctypes_wrapper')))
ff.close()

print("If everything compiled, then run \"bash set_paths.sh\" before using module, and optionally paste paths into your .bashrc file.")
