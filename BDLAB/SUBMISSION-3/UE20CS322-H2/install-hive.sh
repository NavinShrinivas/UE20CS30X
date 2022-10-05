return_to_pwd=$(pwd)
cd
if [ -d "hive" ]; then
    echo "Deleting previous hive installation"
    sudo rm -rf hive
fi

mkdir hive
cd hive

echo "Downloading Hive"
wget https://downloads.apache.org/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz
echo "Unzipping the downloaded package"
tar -xf apache-hive-3.1.3-bin.tar.gz
mv apache-hive-3.1.3-bin apache_hive

echo "Editing bashrc file"
cd
echo "export HIVE_HOME=\$HOME/hive/apache_hive" >> ~/.bashrc
source ~/.bashrc

echo 'HIVE_HOME'
echo $HIVE_HOME
echo "Do you see something like /home/pes1ug20cs999/hive/apache_hive above?[y/n]"
read answer
if [[ $answer == "y" || $answer == "yes" ]]; then
    echo "You're good to go. Run start-hive.sh to start hive. For now, wait for this process to complete for some post-installation steps."
    echo "export PATH=\$PATH:\$HIVE_HOME/bin:$return_to_pwd" >> ~/.bashrc
    source ~/.bashrc
else
    echo "Run source ~/.bashrc and make sure HIVE_HOME is set. For now, wait for this process to complete for some post-installation steps."
    echo "After HIVE_HOME is set, add the following line to bashrc as well: export PATH=\$PATH:\$HIVE_HOME/bin:$return_to_pwd. Once done, run source ~/.bashrc"
    echo "Finally, run start-hive.sh to start hive."
fi

jps_count=$(jps | wc -l)
if [ $jps_count == 1 ]; then
    echo "Starting Hadoop"
    $HADOOP_HOME/sbin/start-all.sh
fi

jps_count=$(jps | wc -l)
if [ $jps_count -lt 6 ]; then
    echo "Hadoop startup failed. Exiting"
    jps
    exit 1
fi
hdfs dfs -test -d /root/hive/warehouse
if [ $? == 0 ]; then
    hdfs dfs -rm -r -f /root*
fi
hdfs dfs -mkdir -p /root/hive/warehouse

cd $return_to_pwd
echo "Finished hive installation. You can use this script again anytime if the installation is broken"