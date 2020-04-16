/*
 * @lc app=leetcode.cn id=83 lang=cpp
 *
 * [83] 删除排序链表中的重复元素
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head==NULL) return head;
        ListNode *temp;
        temp = head;
        while(temp->next!=NULL){
            if(temp->val==temp->next->val){
                temp->next = temp->next->next;
            }
            else {
                temp = temp->next;
            }
        }
        return head;
    }
};
// @lc code=end

