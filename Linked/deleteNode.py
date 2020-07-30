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
            print(node.data)

def deleteNode(head, position):
    temp = head
    if temp is None:
        return
    elif position == 0:
        head = head.next
    else:
        count = 0
        while count < position - 1:
            temp = temp.next
            count += 1
        t = temp
        u = temp.next
        temp.next = u.next
    return head


if __name__ == '__main__':
    fptr = open('delete_node', 'w')
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    position = int(input())
    llist1 = deleteNode(llist.head, position)
    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')
    fptr.close()
