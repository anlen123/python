/*
 * @lc app=leetcode.cn id=1375 lang=cpp
 *
 * [1375] 灯泡开关 III
 */

// @lc code=start
class Solution {
public:
    int numTimesAllBlue(vector<int>& light) {
        int minn = 1;
        int vis[50000+10];
        for (int i = 0;i<50000+2;i++){
            vis[i]=0;
        }
        int sum = 0;
        for (int i = 1 ;i<light.size();i++){
            if (light[i]<=minn){
                sum++;
            }
            int flag = 0;
            for(int j = minn;j<=light[i]-1;i++){
                if (vis[j]==0){
                    flag=1;
                }
            }
            if (flag==0){
                sum++;
                minn = light[i];
            }
            vis[light[i]]=1;
        }
        return sum;
    }
};
// @lc code=end

