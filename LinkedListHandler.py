# Questão 4 e 6

from LinkedList import LinkedList


class LinkedListHandler:

    def merge_sorted(self, ll1, ll2) -> LinkedList:

        pointerll1 = ll1.head
        pointerll2 = ll2.head

        mergedLinkedList = LinkedList()

        while pointerll1 and pointerll2:

            if pointerll1.data < pointerll2.data:
                mergedLinkedList.insert(pointerll1.data)
                pointerll1 = pointerll1.next

            elif pointerll2.data < pointerll1.data:
                mergedLinkedList.insert(pointerll2.data)
                pointerll2 = pointerll2.next

            else: 
                mergedLinkedList.insert(pointerll1.data)
                pointerll1 = pointerll1.next
                pointerll2 = pointerll2.next

        while pointerll1:
            mergedLinkedList.insert(pointerll1.data)
            pointerll1 = pointerll1.next

        
        while pointerll2:
            mergedLinkedList.insert(pointerll2.data)
            pointerll2 = pointerll2.next

        return mergedLinkedList


# [1 -> 2 -> 6 -> 9]
# [1 -> 3 -> 6 -> 9]
# saída esperada = [ 1 -> 2 -> 3 -> 6 -> 9 ]

linked_list1 = LinkedList()
linked_list2 = LinkedList()


linked_list1.insert(1)
linked_list1.insert(2)
linked_list1.insert(6)
linked_list1.insert(8)


linked_list2.insert(1)
linked_list2.insert(3)
linked_list2.insert(7)


merged_linked_list = LinkedListHandler()

merged_linked_list.merge_sorted(linked_list1, linked_list2).peek()
