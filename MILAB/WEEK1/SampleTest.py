import sys
import importlib
import argparse
import pandas as pd
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--SRN', required=True)

args = parser.parse_args()
subname = args.SRN


try:
    mymodule = importlib.import_module(subname)
except Exception as e:
    print(e)
    print("Rename your written program as YOUR_SRN.py and run python3.7 SampleTest.py --SRN YOUR_SRN ")
    sys.exit()


fill_with_mode = mymodule.fill_with_mode
fill_with_group_average = mymodule.fill_with_group_average
get_rows_greater_than_avg = mymodule.get_rows_greater_than_avg


def test_case():
    df = pd.read_csv('example.csv')
    df['Attribute C'].fillna(
        df['Attribute C'].mode()[0], inplace=True)

    try:
        if mymodule.create_numpy_ones_array((2,2)).all()==np.array([[1,1],[1,1]]).all():
            print("Test Case 1 for create_numpy_ones_array PASSED")
        else:
            print("Test Case 1 for create_numpy_ones_array FAILED")
    except Exception as e:
        print("Test Case 1 for create_numpy_ones_array FAILED due to ",e)


    try:
        if mymodule.create_numpy_zeros_array((2,2)).all()==np.array([[0,0],[0,0]]).all():
            print("Test Case 2 for create_numpy_zeros_array PASSED")
        else:
            print("Test Case 2 for create_numpy_zeros_array FAILED")
    except Exception as e:
        print("Test Case 2 for create_numpy_zeros_array FAILED due to ",e) 

    try:
        if mymodule.create_identity_numpy_array(2).all()==np.array([[1,0],[0,1]]).all():
            print("Test Case 3 for create_identity_numpy_array PASSED")
        else:
            print("Test Case 3 for create_identity_numpy_array FAILED")
    except Exception as e:
        print("Test Case 3 for create_identity_numpy_array FAILED due to ",e)  

    try:
        if mymodule.matrix_cofactor(np.array([[4,6],[8,5]])).all()==np.array([[ 5., -8.],[-6. , 4.]]).all():
            print("Test Case 4 for matrix_cofactor PASSED")
        else:
            print("Test Case 4 for matrix_cofactor FAILED")
    except Exception as e:
        print("Test Case 4 for matrix_cofactor FAILED due to ",e)

    try:
        if mymodule.f1(np.array([[1,2],[3,4]]),3,np.array([[1,2],[3,4]]),2,1,2,3,(3,2),(3,2)).all()==np.array([[415.11116764, 604.9332781 ],[187.42695991 ,273.27266349],[112.57538713, 163.6775407 ]]).all():
            print("Test Case 5 for f1 PASSED")
        else:
            print("Test Case 5 for f1 FAILED")
    except Exception as e:
        print("Test Case 5 for f1 FAILED due to ",e)

    try:
        if mymodule.f1(np.array([[1,2],[3,4]]),3,np.array([[1,2],[3,4]]),2,1,2,3,(3,2),(4,2))==-1:
            print("Test Case 6 for f1 PASSED")
        else:
            print("Test Case 6 for f1 FAILED")
    except Exception as e:
        print("Test Case 6 for f1 FAILED due to ",e)

    try:
        if fill_with_mode('example.csv', 'Attribute C').equals(df):
            print("Test Case 7 for the function fill_with_mode PASSED")
        else:
            print("Test Case 7 for the function fill_with_mode FAILED")
    except:
        print("Test Case 7 for the function fill_with_mode FAILED")

    df_copy = df.copy()
    df['Attribute A'].fillna(df.groupby(
        'Attribute C')['Attribute A'].transform('mean'), inplace=True)

    try:
        if fill_with_group_average(df_copy, 'Attribute C', 'Attribute A').equals(df):
            print("Test Case 8 for the function fill_with_group_average PASSED")
        else:
            print("Test Case 8 for the function fill_with_group_average FAILED")
    except:
        print("Test Case 8 for the function fill_with_group_average FAILED")

    df_copy = df[df['Attribute B'] > df['Attribute B'].mean()]

    try:
        if get_rows_greater_than_avg(df, 'Attribute B').equals(df_copy):
            print("Test Case 9 for the function get_rows_greater_than_avg PASSED")
        else:
            print("Test Case 9 for the function get_rows_greater_than_avg FAILED")
    except:
        print("Test Case 9 for the function get_rows_greater_than_avg FAILED")


if __name__ == "__main__":
    test_case()
