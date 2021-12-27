from Posts import Posts
import json

def main():
    # posts = Posts(site='sfbay',
    #               area='scz',
    #               category='apa').getPosts()
    posts = Posts()
    posts.countPosts()
    posts.getPosts()
    return 
    


main()