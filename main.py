import os

import pandas
import requests

AID = os.environ['AID']
API_TOKEN = os.environ['API_TOKEN']
API_URL = 'https://sandbox.piano.io/id/api/v1/publisher/users/get'
headers = {
    'Authorization': API_TOKEN,
}


# reading CSV files
data_file_a = pandas.read_csv('file_a.csv')
data_file_b = pandas.read_csv('file_b.csv')


# merge both files before change
merged_data = pandas.merge(data_file_a, data_file_b, on=('user_id'))
# print(data_merged_file)
# print('------------------------------------')


# iter through emails in merged file, use each as a parameter
# Get User profile by Uid or Email
for user_email in merged_data['email']:
    parameters = {
        'aid': AID,
        'email': user_email,
    }

    # post request to get user profile by email as param
    response = requests.post(API_URL, params=parameters, headers=headers)
    data = response.json()
    # print(data)

    # if user_id is different update, else remains same
    try:
        merged_data['user_id'][merged_data['email'] == user_email] = data['uid']

    except KeyError:
        continue

# print(data_merged_file)


# create CSV file from merged data
merged_data.to_csv('merged_file.csv', index=False)


#API Ref URL: 
# https://docs.piano.io/api/?endpoint=post~2F~2Fpublisher~2Fusers~2Fget#:~:text=Get%20User%20profile%20by%20Uid%20or%20Email

