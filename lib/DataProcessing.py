import pandas as pd
import json

class DataProcessing():
    """
    df: pandas dataframe with an array of posts from cl
    """
    def __init__(self):
        self.data=[]
        self.df = None

    def jsonToPd(self):
        self.df = pd.DataFrame(self.data)
        return self.df

    def formatPrice(self):
        self.df['price']=[int(i.replace("$","").replace(",","")) for i in self.df['price'] if type(i) != int]
        return self.df

    def savePostsToFile(self, filename="posts.json"):
        print("Saving to File {}".format(filename))
        with open(filename, 'w') as f:
            if len(self.data) > 0:
                for post in self.data:
                    json.dump(post, f)
                    f.write("\n")
            elif len(self.data) == 0:
                print("No posts retrieved yet")
            else:
                raise ValueError
        f.close()
        return

    def getPostsFromFile(self, filename="posts.json"):
        print("Getting posts from file {}".format(filename))
        t=[]
        lines = open(filename).read().splitlines()
        for i in lines:
            t.append(json.loads(i))
        self.data = t
        return t

    
