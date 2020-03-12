/*
 * @lc app=leetcode.cn id=1374 lang=cpp
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */

// @lc code=start
class Solution {
public:
    string generateTheString(int n) {
        string s;
        if (n==0){
            return "";
        }
        if(n&1){
            for(int i = 0;i<n;i++){
                s+='a';
            }
        }
        else{
            s+='a';
            for(int i = 0;i<n-1;i++){
                s+='b';
            }
        }
        return s;
    }
};
// @lc code=end

