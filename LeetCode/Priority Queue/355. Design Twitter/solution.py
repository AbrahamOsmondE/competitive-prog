class Twitter(object):

    def __init__(self):
        self.followMap = collections.defaultdict(set)
        for i in range(1, 501):
            self.followMap[i].add(i)
        self.tweets = collections.defaultdict(list)
        self.currTweet = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        curr = self.tweets[userId]
        if len(curr) == 10:
            heapq.heappushpop(curr, (self.currTweet, tweetId))
        else:
            heapq.heappush(curr, (self.currTweet, tweetId))

        self.currTweet += 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        ans = []
        for followed in self.followMap[userId]:
            for tweet in self.tweets[followed]:
                if len(ans) == 10:
                    heapq.heappushpop(ans, tweet)
                else:
                    heapq.heappush(ans, tweet)
        ans.sort(key=lambda i: -1 * i[0])
        return [tweet[1] for tweet in ans]
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)
    
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)