import os
from pathlib import Path

list_of_files=[
    "MCQGenerator/__init__.py",
    "MCQGenerator/MCQGenerator.py",
    "MCQGenerator/logger.py",
    "MCQGenerator/utils.py",
    "research/experiments.ipynb",
    "StreamlitApp.py",
    "test.py",
    "setup.py",
    "requirements.txt"
    ]


for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass