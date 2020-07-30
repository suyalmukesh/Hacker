# This is tough for me
# Dated: 26/07/2020
# #######################################
#!/bin/python3
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def reverse(head):
    if head is None:
        return
    while head.next is None:
        return head

    pre = None
    curr = head
    nextnode = None

    while curr is not None:
        nextnode = curr.next
        curr.next = pre
        pre = curr
        curr = nextnode

    head = pre
    return head


if __name__ == '__main__':
    fptr = open('Reverse_Link', 'w')
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        llist1 = reverse(llist.head)
        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')
    fptr.close()
