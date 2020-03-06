#!/usr/bin/env bash
python create_dvc_dag.py data/data1.csv models/model_1.csv
python create_dvc_dag.py data/data2.csv models/model_2.csv
python create_dvc_dag.py data/data3.csv models/model_3.csv
