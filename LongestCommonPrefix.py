'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        pr=[]
        if len(strs)==1:
            return strs[0]
        try:
            leng=len(strs[0])
        except:
            return ""
        if leng==0:
            return ""
        for j in range(leng):
            temp=strs[0][j]
            for i in range(1,len(strs)):
                try:
                    if strs[i][j]==temp:
                        pass
                    else:
                        return ''.join(pr) if len(pr)!=0 else ""
                        break
                except:
                    return ''.join(pr) if len(pr)!=0 else ""
            pr.append(temp)
        return ''.join(pr) if len(pr)!=0 else ""
