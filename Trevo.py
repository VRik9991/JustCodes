class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class GeneralBinaryTree:
    def __init__(self):
        self.root = None

    def append(self, value, node=None):
        if self.root is None:
            self.root = Node(value)
            return
        if node is None:
            node = self.root
        if value >= node.value:
            if node.right is not None:
                self.append(value, node=node.right)
            else:
                node.right = Node(value)
        else:
            if node.left is not None:
                self.append(value,node=node.left)
            else:
                node.left = Node(value)
    def __str__(self,node=None):
        stop = False
        lefta = []
        if node is None:
            node = self.root
        if node.left is not None and not stop:
            lefta.append(node.left.value)
            lefta + self.__str__(node.left)
        if node.right is not None:
            return [] + lefta + [node.value] + self.__str__(node.right)
        elif stop:
            return [] + lefta
        else:
            stop = True
            return [] + lefta + self.__str__()









gbt = GeneralBinaryTree()
gbt.append(3)
gbt.append(6)
gbt.append(1)
gbt.append(8)
print(gbt)

# 1+

# # 5 + (4 + (3 + (2 + 1 + 0))))
# def get_num_summ(n):
#     if n == 0:
#         return 0
#     return n + get_num_summ(n - 1)

#
# print(get_num_summ(5))