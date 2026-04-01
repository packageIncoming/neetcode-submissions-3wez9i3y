'''
Implement a simplified version of Twitter which allows users
to post tweets, 
    -Add only 
follow/unfollow each other, 
- Add and remove (perhaps from a set)
and view the 10 most recent tweets within their own news feed.
- Maxheap where the posts are [postCounter, (postinfo)]

void postTweet(int userId, int tweetId) 
Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
    -Push to the maxheap
    - Need to include a postCounter variable within the Twitter object

List<Integer> getNewsFeed(int userId)
     Fetches at most the 10 most recent tweet IDs in the user's news feed
        -Pop from the  maxheap
    Each item must be posted by users who the user is following or by the user themself
        -Get the set of followed users and include the user ID, check each popped item to make sure it
        is in the list of valid tweets
    Tweets IDs should be ordered from most recent to least recent
        - Structure of maxheap implies that items will be popped most to least recent
void follow(int followerId, int followeeId)
    The user with ID followerId follows the user with ID followeeId.
        - Simply add to set in following hashmap
void unfollow(int followerId, int followeeId) 
    The user with ID followerId unfollows the user with ID followeeId.
        -Simply remove from set in following hashmap

Object Data:
    - postCounter: internal counter for ordering tweets, starts at 0 and decrements for each tweet
        * decrement since maxheap ordered by negative values 
    - tweets_max_heap: max heap containing tweets
        -(tweet object): [postCounter, userId, tweetId]
    - userFollowing: hashmap {userId: followingSet} where followingSet is the set of users that userId
        follows
'''

class Twitter:

    def __init__(self):
        self.postCounter = 0
        self.tweets_max_heap = []
        self.userFollowing = defaultdict(set) # {userA: set of users that userA follows}

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [self.postCounter,userId,tweetId]
        heapq.heappush(self.tweets_max_heap,tweet)
        self.postCounter-=1


    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        seen = []
        usersFollowed = self.userFollowing[userId]
        while len(self.tweets_max_heap)>0 and len(newsFeed) < 10:
            top  = heapq.heappop(self.tweets_max_heap)
            print(top)
            if top[1] in usersFollowed or top[1] == userId:
                newsFeed.append(top[2])
                seen.append(top)
            else:
                seen.append(top)
        # reinsert tweets after search
        for t in seen:
            heapq.heappush(self.tweets_max_heap,t)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.userFollowing[followerId]:
            self.userFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowing[followerId]:
            self.userFollowing[followerId].remove(followeeId)
