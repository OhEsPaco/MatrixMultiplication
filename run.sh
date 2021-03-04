#!/bin/bash

rm -rf MatrixMultiplication

hdfs dfs -mkdir MatrixMultiplication

hdfs dfs -copyFromLocal example1.txt MatrixMultiplication/example1.txt

hdfs dfs -copyFromLocal example2.txt MatrixMultiplication/example2.txt

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
-mapper "python mapper.py" \
-reducer "python reducer.py" \
-input MatrixMultiplication/example1.txt \
-output MatrixMultiplication/out1

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
-mapper "python mapper.py" \
-reducer "python reducer.py" \
-input MatrixMultiplication/example2.txt \
-output MatrixMultiplication/out2
