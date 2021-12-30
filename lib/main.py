from Posts import Posts
from DataProcessing import DataProcessing
from Metrics import Metrics


def main():

    # posts = Posts()
    # posts.getPosts()

    
    data = DataProcessing()
    # data.data=posts.housingPosts
    data.getPostsFromFile()
    # data.savePostsToFile()
    data.jsonToPd()
    data.formatPrice()
    
    metrics = Metrics(data.df)
    metrics.avgPrice()
    metrics.countPerBedroom()
    metrics.countPostsPerWhere()
    
    return 
    


main()