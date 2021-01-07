import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        #dict의 모양이 list인 형태로 init
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        #애니어그램은 어차피 들어있는 글자는 다 똑같으므로 정렬한 후의 값을 키로 지정하고 그 키가 같으면 값을 append
            
        return list(anagrams.values())
        #sorted로 정렬된 key는 기존 값과 다르므로 원래 값이 있는 values()

#https://leetcode.com/problems/group-anagrams/
