from CraigslistHousingWrapper import CraigslistHousingWrapper
import json

class Posts(CraigslistHousingWrapper):

    housingPosts=[]

    def craigslistClient(self): 
        return CraigslistHousingWrapper(site=self.site, 
                                        area=self.area, 
                                        category=self.category)

    def countPosts(self):
        craigslistClient = self.craigslistClient()
        countPosts = craigslistClient.get_results_approx_count()
        print("There are approximately {} Posts".format(str(countPosts)))
        return countPosts

    def getPosts(self):
        craigslistClient = self.craigslistClient()
        for result in craigslistClient.get_results(sort_by='newest', geotagged=True, limit=10):
            self.housingPosts.append(result)
        print(json.dumps(self.housingPosts,indent=4))
        return self.housingPosts

    def savePostsToFile(self, filename):
        print("Saving to File {}".format(filename))
        with open(filename, 'w') as f:
            if len(self.housingPosts) > 0:
                for post in self.housingPosts:
                    json.dump(post, f, indent=4)
            elif len(self.housingPosts) == 0:
                print("No posts retrieved yet")
            else:
                raise ValueError
        f.close()
        return
                
