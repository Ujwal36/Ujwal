def findDifference(nums1, nums2) :
        answer1 = []
        answer2 = []
        answer = []
        for val in nums1:
            if val not in nums2:
                answer1.append(val)
        print(answer1)
        for val in nums2:
            if val not in nums1:
                answer2.append(val)
        print(answer2)
        answer.append(answer1)
        answer.append(answer2)
        print(answer)
        return answer
nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1,nums2))