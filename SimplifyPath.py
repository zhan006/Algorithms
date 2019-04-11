'''Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.'''
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        import re
        pattern=r'/([a-z A-Z . _ \d]+)'
        pth=re.findall(pattern,path)
        if len(pth)==0:
            return '/'
        order=-1
        res=[]
        for i in range(len(pth)):
            if order==-1:
                if pth[i]=='..' or pth[i]=='.':
                    pass
                else:
                    order+=1
                    res.append(pth[i])

            else:
                if pth[i]=='..':
                    order-=1
                    res.pop()
                elif pth[i]=='.':
                    pass
                else:
                    order+=1
                    res.append(pth[i])
        res='/'+'/'.join(res)
        return res
    