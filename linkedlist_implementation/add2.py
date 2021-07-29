"""
File: add2.py
Name: 吳采曄 Judy Wu
------------------------
Given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
This program adds the two numbers and return the sum as a linked list in reverse order.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    :param l1: the first ListNode input, representing a non-negative interger.
    :param l2: the second ListNode input, representing a non-negative interger.
    :return: a ListNode that is the sum of l1 and l2.
    """
    #######################
    cur1 = l1                                         # assign cur1 as l1 to run linked list implementation
    lst1 = []                                         # assign lst1 as an empty list
    ans1 = 0                                          # assign ans1 as the real integer represented by l1
    while cur1 is not None:
        lst1.append(cur1.val)                         # append each cur1's value into lst1
        cur1 = cur1.next
    for i in range(len(lst1)):
        ans1 += lst1[i] * (10 ** i)                   # ans1 equals the sum of lst1's digit times different power of 10

    cur2 = l2                                         # assign cur2 as l2 to run linked list implementation
    lst2 = []                                         # assign lst2 as an empty list
    ans2 = 0                                          # assign ans2 as the real integer represented by l2
    while cur2 is not None:
        lst2.append(cur2.val)                         # append each cur2's value into lst2
        cur2 = cur2.next
    for j in range(len(lst2)):
        ans2 += lst2[j] * (10 ** j)                   # ans2 equals the sum of lst2's digit times different power of 10

    ans = ans1 + ans2                                 # real ans is sum of ans1 and ans2
    ans_lst = None                                    # assign ans_lst as None
    cur = None                                        # assign cur as None to run linked list implementation
    if ans == 0:                                      # if ans is 0, ans_lst only contains 1 ListNode: 0.
        ans_lst = ListNode(ans, None)
    else:
        while ans != 0:                               # while ans still has digit
            digit = ans % 10                          # each digit is the remainder of n divided by 10
            if ans_lst is None:                       # first data
                ans_lst = ListNode(digit, None)       # assign first data as ans_lst
                cur = ans_lst
            else:                                     # second and more data
                cur.next = ListNode(digit, None)      # use cur to add more ListNode into ans_lst
                cur = cur.next
            ans = int(ans // 10)                      # update n value to make it closer to 0
    #######################
    return ans_lst


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
