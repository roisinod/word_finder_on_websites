import urllib #imports library for working with data from URLs
import requests #imports module of urllib for opening and reading URLs
import pandas as pd #imports pandas library under the name pd. This will be used later for creating aesthetically pleasing dataframe
import re
websitename = str(input('Type in your url...')) #asks user to input URL and stores URL in variable websitename
website = requests.get(websitename).text #creates a variable called 'website'. This contains the URL for the website the user has entered, gathers the data of chosen website and reads it as a .text file.
wordtofind = str(input('Type in what word you would like to find...')) #asks the user what word they would like to find and stores the request in variable wordtofind
findonwebsite = re.findall(wordtofind, website) #creates another variable. It finds all occurances on of the word 'ECCO' on the web page. It is case sensitive.
print('------')
print('This words occurs', len(findonwebsite), 'times')#prints the number of times this word occurs on the page
print('------')
df = pd.DataFrame() #creates a variable that hosts a pandas dataframe.
df['List'] = findonwebsite #using the data gathered from the variable 'findonwebsite' it creates a list/dataframe. It is given the simple title list
df #prints List