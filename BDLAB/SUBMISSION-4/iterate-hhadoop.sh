#!/bin/sh
CONVERGE=1
ITER=1
rm w w1 log*
$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /temp_test/output*


$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
  -mapper "/home/pes2ug20cs237/test/map.py"\
  -reducer "/home/pes2ug20cs237/test/red.py /home/pes2ug20cs237/test/w"\
  -input "/temp_test/web-Google.txt"\
  -output "/temp_test/output1"

while [ "$CONVERGE" -ne 0 ] 
do
  echo "############################# ITERATION $ITER #############################"
  $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
  -mapper "/home/pes2ug20cs237/test/map2.py /home/pes2ug20cs237/test/w /home/pes2ug20cs237/test/page_embeddings.json"\
  -reducer "/home/pes2ug20cs237/test/red2.py"\
  -input "/temp_test/output1/part-00000"\
  -output "/temp_test/output2"
  touch w1
  hadoop dfs -cat /temp_test/output2/part-00000 > "$PWD/w1"
  CONVERGE=$(python3 ./check_conv.py $ITER>&1)
  ITER=$((ITER+1))
  hdfs dfs -rm -r /temp_test/output2
  echo $CONVERGE
done
