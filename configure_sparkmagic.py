from subprocess import call
import os

sparkmagic_config = r"""
{
  "kernel_python_credentials" : {
    "username": "",
    "password": "",
    "url": "http://10.30.1.32:8998"
  },

  "kernel_scala_credentials" : {
    "username": "",
    "password": "",
    "url": "http://10.30.1.32:8998"
  },

  "logging_config": {
    "version": 1,
    "formatters": {
      "magicsFormatter": {
        "format": "%(asctime)s\t%(levelname)s\t%(message)s",
        "datefmt": ""
      }
    },
    "handlers": {
      "magicsHandler": {
        "class": "hdijupyterutils.filehandler.MagicsFileHandler",
        "formatter": "magicsFormatter",
        "home_path": "~/.sparkmagic"
      }
    },
    "loggers": {
      "magicsLogger": {
        "handlers": ["magicsHandler"],
        "level": "DEBUG",
        "propagate": 0
      }
    }
  },

  "wait_for_idle_timeout_seconds": 15,
  "status_sleep_seconds": 2,
  "statement_sleep_seconds": 2,
  "livy_session_startup_timeout_seconds": 60,

  "fatal_error_suggestion": "The code failed because of a fatal error:{}",

  "ignore_ssl_errors": false,

  "session_configs": {
    "driverMemory": "1000M",
    "executorCores": 2,
    "conf":{"spark.jars.packages":"org.apache.hadoop:hadoop-aws:2.7.3,org.apache.hadoop:hadoop-azure:2.7.3"}
  },

  "use_auto_viz": true,
  "max_results_sql": 2500,
  "pyspark_dataframe_encoding": "utf-8",

  "heartbeat_refresh_seconds": 30,
  "livy_server_heartbeat_timeout_seconds": 0,
  "heartbeat_retry_seconds": 10,

  "server_extension_default_kernel_name": "pysparkkernel"
}
"""
os.mkdir("/home/jupyter/.sparkmagic")
os.mkdir("/root/.sparkmagic")
sparkmagic_config_file = open("/home/jupyter/.sparkmagic/config.json", "w")
sparkmagic_config_file.write(sparkmagic_config)
sparkmagic_config_file.close()
sparkmagic_config_file = open("/root/.sparkmagic/config.json", "w")
sparkmagic_config_file.write(sparkmagic_config)
sparkmagic_config_file.close()
call(["jupyter", "notebook", "--generate-config"])
call(["pip", "install", "sparkmagic"])
call(["pip3", "install", "sparkmagic"])
call(["jupyter", "nbextension", "enable", "--py", "--sys-prefix", "widgetsnbextension"])
call(["jupyter", "serverextension", "enable", "--py", "sparkmagic"])
call(["jupyter-kernelspec", "install", "/usr/local/lib/python3.5/dist-packages/sparkmagic/kernels/sparkkernel"])
call(["jupyter-kernelspec", "install", "/usr/local/lib/python2.7/dist-packages/sparkmagic/kernels/sparkkernel"])
call(["apt-get", "update"])
call(["apt-get", "install", "jq"])