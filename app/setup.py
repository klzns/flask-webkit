# import sys, glob, os
# from cx_Freeze import setup, Executable

# include_files = []
# basedir = os.path.dirname(__file__)
# include_files += (glob.glob(os.path.join(basedir, 'templates/**/*')))
# include_files += (glob.glob(os.path.join(basedir, 'static/**/*')))

# include_files += (glob.glob(os.path.join(basedir, 'app.db')))
# include_in_shared_zip = (glob.glob(os.path.join(basedir, 'app.db')))

# # Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {
# 	"packages": ["atexit", "PySide.QtNetwork"],
# 	"excludes": ["tkinter"],
# 	"include_files": include_files,
# 	"include_in_shared_zip": include_in_shared_zip,
# 	"copy_dependent_files": True
# }

# # GUI applications require a different base on Windows (the default is for a
# # console application).
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

# setup(  name = "desktopapp",
#         version = "1.0",
#         description = "My desktop-flask application!",
#         options = {"build_exe": build_exe_options},
#         executables = [Executable("app/desktopapp.py", base=base)])


from setuptools import setup, find_packages

setup(
    name='Your Application',
    version='1.0',
    long_description=__doc__,
    packages=['app', 'app.resources'],
    scripts = ['app/run.py'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
	    'Flask==0.10.1',
		'SQLAlchemy==0.9.4'
	]
)