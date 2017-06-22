sudo apt-get update
sudo apt-get -y install wget
wget http://apache.cs.utah.edu/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
tar -xf hadoop-2.7.3.tar.gz
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
hadoop-2.7.3/bin/hdfs dfs -copyFromLocal -f /home/jupyter/modeldb/client/scala/libs/spark.ml/target/scala-2.11/modeldb-scala-client.jar $AWS_EMR_HDFS/data
hadoop-2.7.3/bin/hdfs dfs -ls $AWS_EMR_HDFS/data
