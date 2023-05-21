n = 37

class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        def dfs(s, i, n, v, dp):
            if i==n:
                if v==0: return True
                return False
            kk = (i, v)
            if kk in dp: return dp[kk]
            r = False

            j=i
            vv=0
            while j<n:
                vv=vv*10+s[j]
                if vv>v: break
                if dfs(s, j+1, n, v-vv, dp):
                    r=True
                    break
                j+=1
            dp[kk]=r
            return r
        def check(v):
            q = v*v
            s = [ord(c)-ord('0') for c in str(q)]
            if dfs(s, 0, len(s), v, {}): return q
            return 0
        r = 0
        for i in range(1, n+1):
            r+=check(i)
        return r

s = Solution()
print(s.punishmentNumber(n))
