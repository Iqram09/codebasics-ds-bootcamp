import os
import sys

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

print(project_dir)

sys.path.append(project_dir)