sudo apt-get update
sudo apt-get -y install wget
wget https://github.com/sbt/sbt/releases/download/v0.13.15/sbt-0.13.15.tgz
tar -xf sbt-0.13.15.tgz
export PATH=$PATH:/home/jupyter/sbt/bin
sudo apt-get -y install openjdk-8-jdk-headless
git clone https://github.com/mitdbg/modeldb.git
