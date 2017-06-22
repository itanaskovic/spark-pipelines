from subprocess import call
import os
cwd = os.getcwd()
call(["python", "configure_sparkmagic.py"])
call(["sudo", "-u", "jupyter", "jupyter", "nbconvert",  "--config", cwd + "/.jupyter/jupyter_notebook_config.py", "--ExecutePreprocessor.timeout=600", "--to", "notebook", "--output", "/tmp/spark", "--execute", 'Spark ML Pipelines and MLeap Demo.ipynb'])
call(["cat", "/tmp/spark.ipynb"])
call(["jq", ".cells[].outputs[].text?", "/tmp/spark.ipynb"])
