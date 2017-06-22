from subprocess import call
call(["jupyter", "nbconvert",  "--ExecutePreprocessor.timeout=600", "--to", "notebook", "--output", "spark", "--execute", 'Spark ML Pipelines and MLeap Demo.ipynb'])
call(["jq", ".cells[].outputs[].text?", "spark.ipynb"])
