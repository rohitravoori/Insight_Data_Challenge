# Insight Data Challenge

## Rohit Ravoori - rravoor1@jhu.edu

# Overview

For this challenge, I have implemented the donation-analytics code in python with basic libraries which come pre-installed with python. I wasn't able to write any unit test cases due to the lack of time.

# Assumptions

As the size of data has not been mentioned and no specifics regarding the databases have been mentioned for persistant storage, I have assumed that this data can be stored in memory.

# Data Strutures

I have used a 2 dictionaries, 1 to store all the data and 1 to store repeated donation from a particular zip code. For the first dictionary, I have used a tuple of the name and zip code as the key. For the second dictionary I have used a tuple with the Zip code, Recipient ID and Year as the key.

# Algorithm

The dictionaries make the implemenation fairly straight forward. Inserting new enteries and checking for repeated enteries run with a time complexity of O(1) and hence is provides an efficient solution.



