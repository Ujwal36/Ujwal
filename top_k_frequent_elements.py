#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


def topKFrequent(nums, k):
        dict = {}
        list = []
        for ele in nums:
            if ele not in dict.keys():
                dict.update({ele:1})
            else:
                dict.update({ele:dict.get(ele)+1})
        list = [x for x in dict.values()]
        list.sort()
        output = []
        list = list[-k:]
        print(list[-k:])
        for ele in dict.keys():
            if dict.get(ele) in list:
                output.append(ele)
        print(output)
nums = [1,1,1,2,2,2,3,3,3]
k = 2
        
topKFrequent(nums,k)
