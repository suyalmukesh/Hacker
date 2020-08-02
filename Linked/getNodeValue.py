# Simple Problem
# Solved in First attempt
# Dated : 02/08/2020
#####################################

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


def count_list(head):
    count = 0
    if head is None:
        return
    while head is not None:
        count += 1
        head = head.next
    #print(f"Count of list is {count}")
    return count


def getNode(head, positionFromTail):
    n = count_list(head)
    if n is None:
        return
    position = n - positionFromTail
    #print(f"position is {position}")
    count = 0
    temp = head
    while count < position-1:
        temp = temp.next
        count +=1
    #print(temp.data)
    return temp.data


if __name__ == '__main__':
    fptr = open('OUTPUT/getnodevalue', 'w')
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        position = int(input())
        result = getNode(llist.head, position)
        fptr.write(str(result) + '\n')
    fptr.close()
