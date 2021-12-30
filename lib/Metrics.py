import json
import pandas as pd
"""
Start off class with an array of dictionaries, which is the output 
from getPosts()
"""

class Metrics():
    def __init__(self, df):
        self.df=df
   
    def avgPrice(self):
        """
        select num_bedrooms, sum(price) from df group by 1;
        """
        result = self.df[['bedrooms','price']].groupby("bedrooms").mean("price")
        print(result)
        return result

    def countPerBedroom(self):
        """
        select num_bedrooms, count(distinct id) from df group by 1;
        """
        print("How many studios, 1 Bed, 2 Bed, 3 Bed etc units available")
        result = self.df.groupby('bedrooms').size()
        print(result)
        return result
 
    def countPostsPerWhere(self):
        """
        select where, count(distinct id) from df group by 1;
        """
        print("Breakdown of Posts per Area in Santa Cruz County")
        result = self.df.groupby('where').size()
        print(result)
        return result