#!/usr/bin/env python3

import pyspark
from pyspark.sql.functions import *

import sys

input_file_csv = sys.argv[1]
output_file_csv = sys.argv[2]

# conf = pyspark.SparkConf().setMaster("yarn")
# spark_ctx = pyspark.SparkContext.getOrCreate(conf)
spark_ctx = pyspark.sql.SparkSession.builder.appName("solution").getOrCreate()
init_dataframe = spark_ctx.read.csv(input_file_csv, header=True, inferSchema=True)
init_dataframe = init_dataframe.distinct()
average_df = init_dataframe.groupBy("RP State Plate").agg(avg("Fine amount")).where(col("RP State Plate") != "")
joint_df = init_dataframe.join(average_df, ["RP State Plate"], "fullouter")
joint_df = joint_df.na.drop(how="any", thresh=None, subset=None)
output_df = joint_df.select(joint_df["Ticket number"]).where(joint_df["Color"] == "WH").where(joint_df["Fine amount"] > joint_df["Avg(Fine amount)"]).orderBy("Ticket number")
output_df.write.format("csv").save(output_file_csv)

