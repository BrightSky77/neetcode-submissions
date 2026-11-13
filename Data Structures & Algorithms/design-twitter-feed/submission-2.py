class Twitter:
    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((-self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Include the user themselves so their own tweets appear in the feed
        self.followMap[userId].add(userId)

        # Push the most recent tweet from each followee onto the heap
        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId])-1
                time,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,(time,tweetId,followeeId,index))
        
        while minHeap and len(res)<10:
            time,tweetId,followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            index -= 1
            if index >= 0:
                time,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,(time,tweetId,followeeId,index))
            

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
