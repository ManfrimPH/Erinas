class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        # Passo 1: inserção normal de BST
        if not root:
            return Node(key)
        elif list(key.keys())[0] < list(root.key.keys())[0]:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Passo 2: atualizar altura do nó atual
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Passo 3: obter fator de balanceamento
        balance = self.get_balance(root)

        # Passo 4: balancear se necessário

        # Rotação simples à direita
        if balance > 1 and list(key.keys())[0] < list(root.left.key.keys())[0]:
            return self.right_rotate(root)

        # Rotação simples à esquerda
        if balance < -1 and list(key.keys())[0] > list(root.right.key.keys())[0]:
            return self.left_rotate(root)

        # Rotação dupla esquerda-direita
        if balance > 1 and list(key.keys())[0] > list(root.left.key.keys())[0]:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Rotação dupla direita-esquerda
        if balance < -1 and list(key.keys())[0] < list(root.right.key.keys())[0]:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Rotação
        y.left = z
        z.right = T2

        # Atualizar alturas
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Rotação
        y.right = z
        z.left = T3

        # Atualizar alturas
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.key, end=' ')
            self.in_order(root.right)

    def search(self, root, key):
        if not root:
            return None
        if key == (list(root.key.keys())[0]):
            return root.key
        elif key < (list(root.key.keys())[0]):
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
        
    def search_update(self, root, key, new_value):
        if not root:
            return None
        if key == (list(root.key.keys())[0]):
            root.key = new_value
            return root
        elif key < (list(root.key.keys())[0]):
            return self.search_update(root.left, key, new_value)
        else:
            return self.search_update(root.right, key, new_value)
        
    def pretty_print(self, node, prefix="", is_left=True):
        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            self.pretty_print(node.right, new_prefix, False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.pretty_print(node.left, new_prefix, True)
