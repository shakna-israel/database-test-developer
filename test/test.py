import nose
import os

nose.config.Config.srcDirs = (os.getcwd())
nose.run(argv=["","test/librarian/Book.py"])
