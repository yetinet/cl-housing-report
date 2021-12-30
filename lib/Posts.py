from CraigslistHousingWrapper import CraigslistHousingWrapper
import json

class Posts():
    def __init__(self):
        self.client = CraigslistHousingWrapper()
        self.housingPosts = []

    def countPosts(self):
        craigslistClient = self.client #self.craigslistClient()
        countPosts = craigslistClient.get_results_approx_count()
        print("There are approximately {} Posts".format(str(countPosts)))
        return countPosts

    def getPosts(self):
        craigslistClient = self.client #self.craigslistClient()
        for result in craigslistClient.get_results(sort_by='newest', 
                                                   geotagged=True, 
                                                   include_details=True, 
                                                   limit=1000):
            self.housingPosts.append(result)      
        print(json.dumps(self.housingPosts,indent=4))
        return self.housingPosts

    def savePostsToFile(self, filename="posts.jsons"):
        print("Saving to File {}".format(filename))
        with open(filename, 'w') as f:
            if len(self.housingPosts) > 0:
                for post in self.housingPosts:
                    json.dump(post, f)
                    f.write("\n")
            elif len(self.housingPosts) == 0:
                print("No posts retrieved yet")
            else:
                raise ValueError
        f.close()
        return

    # TODO
    # def getPostsFromFile(self, filename="posts.json"):
    #     print("Getting posts from file {}".format(filename))
    #     with open(filename, 'r') as f:
    #         js = json.loads(f.read())
        # f.close()
    #     return js
