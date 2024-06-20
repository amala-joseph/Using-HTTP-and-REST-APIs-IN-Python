# -*- coding: utf-8 -*-
"""HTTP & PYTHON API.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zP1izqn9CLYZb9GjhO_gidG0S2wSWYAt
"""

#Requests is a Python Library that allows you to send HTTP/1.1 requests easily. We can import the library as follows:


import requests
import os
from PIL import Image
from IPython.display import IFrame

#defining the url
url='https://www.ibm.com/'
#get method to get the structure and data in the url
r=requests.get(url)
#We have the response object r, this has information about the request, like the status of the request. We can view the status code using the attribute status_code.
print("Status Code : ",r.status_code)

#We can view the request headers using the method headers
print("Header : ",r.headers)
header=r.headers
#We can view the request body using the method content
print("Body : ",r.request.body)

#We can view the request url using the method url
print("URL : ",r.url)
#We can obtain the date the request was sent using the key Date.
print("Header Date : ",header['date'])
#Content-Type indicates the type of data:
print("Header Content type : ",header['Content-Type'])
#You can also check the encoding
print("Encoding : ",r.encoding)
#As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
print("reviewing the first 100 characters in the html page : ",r.text[0:100])

#You can load other types of data for non-text requests, like images. Consider the URL of the following image:
# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
#We can make a get request:
r=requests.get(url)
#We can view the header information:
print("Header : ",r.headers)
#We can see the 'Content-Type'
print("Header Content type : ",r.headers['Content-Type'])
#n image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')
#Then, we open the file object, write the image to it, and close the file
with open(path,'wb') as f:
    f.write(r.content)
#We can view the image:
Image.open(path)

#Consider the following URL.
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
#Write the commands to download the txt file in the given link.
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(URL)
with open(path,'wb') as f:
    f.write(r.content)

#A query string is a part of a uniform resource locator (URL), this sends other information to the web server. The start of the query is a ?, followed by a series of parameter and value pairs, as shown in the table below. The first parameter name is name and the value is Joseph. The second parameter name is ID and the Value is 123. Each pair, parameter, and value is separated by an equals sign, =. The series of pairs is separated by the ampersand &.
url_get='http://httpbin.org/get'
#To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.
payload={"name":"Joseph","ID":"123"}
#Then passing the dictionary payload to the params parameter of the  get() function:
r=requests.get(url_get,params=payload)
#We can print the response:
print("Request URL: ",r.url)
print("Status Code: ",r.status_code)
print("Header: ",r.headers)
print("Header Content Type : ",r.headers['Content-Type'])
print("Body: ",r.request.body)
print("Text : ",r.text)
print("JSON: ",r.json())
print("JSON: ",r.json()['args'])

#Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:
url_post='http://httpbin.org/post'
response_post=requests.post(url_post,data=payload)
print('Response Text :',response_post.text)
print('Response JSON :',response_post.json())
print('Response Status Code :',response_post.status_code)
print('Response Headers :',response_post.headers)
print('Response URL :',response_post.url)
print('Response History :',response_post.history)
print('Response Cookies :',response_post.cookies)
print('Response Elapsed Time :',response_post.elapsed)
print('Response Encoding :',response_post.encoding)
print('Response Reason :',response_post.reason)
print('Response Request :',response_post.request)
print('Response Raw :',response_post.raw)
print('Response Time :',response_post.elapsed.total_seconds())
print('Response JSON Form:',response_post.json()['form'])

"""Get Methods

get_cell()

get_city()

get_dob()

get_email()

get_first_name()

get_full_name()

get_gender()

get_id()

get_id_number()

get_id_type()

get_info()

get_last_name()

get_login_md5()

get_login_salt()

get_login_sha1()

get_login_sha256()

get_nat()

get_password()

get_phone()

get_picture()

get_postcode()

get_registered()

get_state()

get_street()

get_username()

get_zipcode()

"""

#To start using the API you can install the randomuser library running the pip install command.
!pip install randomuser

#Then, we will load the necessary libraries.
from randomuser import RandomUser
import pandas as pd
#First, we will create a random user object, r.
r = RandomUser()
#Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
#We can view the list.
print(some_list)

#The "Get Methods" functions mentioned at the beginning of this notebook, can generate the required parameters to construct a dataset. For example, to get full name, we call get_full_name() function.
name = r.get_full_name()
#Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.
for i in some_list:
    print(i.get_full_name())
    print(i.get_email())

#In this Exercise, generate photos of the random 10 users.
for useer in some_list:
    print(useer.get_picture())

#To generate a table with information about the users, we can write a function containing all desirable parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.
def get_users():
    users =[]

    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})

    return pd.DataFrame(users)

get_users()

df1 = pd.DataFrame(get_users())
#Now we have a pandas dataframe that can be used for any testing purposes that the tester might have.

#Another, more common way to use APIs, is through requests library. The next lab, Requests and HTTP, will contain more information about requests.We will start by importing all required libraries.
import requests
import json
#We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format.
data=requests.get("https://fruityvice.com/api/freit/all")
#We will retrieve results using json.loads() function
#Check for successful response
if data.status_code == 200:
    results=json.loads(data.text)
    pd.DataFrame(results)
else:
    print("API request failed with status code:", data.status_code)
#The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
print(df2)
#Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
#In this Exercise, find out how many calories are contained in a banana.
banana=df2.loc[df2["name"]=='Banana']
banana.iloc[0]['nutritions.calories']

#Using requests.get("url") function, load the data from the URL.
joke=requests.get("https://official-joke-api.appspot.com/jokes/ten")
#Retrieve results using json.loads() function.
data=json.loads(joke.text)
#Convert json data into pandas data frame. Drop the type and id columns.
joke_data=pd.DataFrame(data)
joke_data.drop(columns=["type","id"],inplace=True)
joke_data

