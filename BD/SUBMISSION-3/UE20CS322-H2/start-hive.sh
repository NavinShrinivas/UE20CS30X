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

hdfs dfsadmin -safemode leave
hdfs dfs -test -d /root/hive/warehouse
if [ $? == 1 ]; then
    hdfs dfs -mkdir -p /root/hive/warehouse
fi

cd

rm -rf metastore_db/

$HIVE_HOME/bin/schematool -initSchema -dbType derby

hive