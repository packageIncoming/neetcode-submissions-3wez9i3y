class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        memo = [[-1]*(len(s2)+1) for i in range(len(s1)+1)] #[s1][s2]

        def dfs_build(s1_idx,s2_idx,s3_idx):
            if s3_idx == len(s3):
                return True
            if memo[s1_idx][s2_idx]!=-1:
                return memo[s1_idx][s2_idx]

            if s1_idx<len(s1) and s1[s1_idx] == s3[s3_idx] and s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
                memo[s1_idx][s2_idx]= dfs_build(s1_idx+1,s2_idx,s3_idx+1)
                if memo[s1_idx][s2_idx] == True:
                    return memo[s1_idx][s2_idx]
                else:
                    memo[s1_idx][s2_idx]=  dfs_build(s1_idx,s2_idx+1,s3_idx+1)
                return memo[s1_idx][s2_idx]
            elif s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
                # match on s1, move forward s1
                memo[s1_idx][s2_idx]= dfs_build(s1_idx+1,s2_idx,s3_idx+1)
                return memo[s1_idx][s2_idx]
            elif s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
                # match on s2, move forward s2
                
                memo[s1_idx][s2_idx] =  dfs_build(s1_idx,s2_idx+1,s3_idx+1)
                return memo[s1_idx][s2_idx]
            else:
                return False # neither match
        return dfs_build(0,0,0)