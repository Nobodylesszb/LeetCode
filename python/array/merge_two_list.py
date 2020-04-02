# 假设 l1的长度大

class Solution(object):
    def merge_two_list(self,list1,list2):
        result = []
        while list1 and list2:
            if list1[0] < list2[0]:
                result.append(list1[0])
                del list1[0]
            else:
                result.append(list2[0])
                del list2[0]
        if list1:
            result.extend(list1)
        if list2:
            result.extend(list2)
        return result


list1 = [3,4,7,9,11]
list2 = [1,2,5,8,13,20]
s = Solution()
r = s.merge_two_list(list1,list2)
print(r)
        
