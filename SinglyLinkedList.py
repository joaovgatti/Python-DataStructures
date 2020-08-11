class Node:
    """ Esta eh uma classe auxiliar que representa um No da lista encadeada.
        Cada No eh composto por um valor e um ponteiro que aponta para o
        proximo No.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


"""Esta a classe da LinkedList e seus metodos.
Uma linkedList eh composta por uma uniao de nos,
independentes,ligados por ponteiros."""


class LinkedList:
    def __init__(self):
        self.head = None

    # Este Metodo adiciona um elemento no inicio da linkedList.
    def insertAtBeginning(self, value):
        # Cria-se um um novo no e armazena-se o valor desejado nele.
        temp = Node(value)
        # Como este no vai ser a Head,o seu proximo aponta para a Head original.
        temp.next = self.head
        # Head passa a ser o novo No criado.
        self.head = temp

    # Este Metodo insere um elemento apos um ja existente na linkedlist.
    def insertAfterGivenNode(self, prev_node, value):
        # confere se o no ja existente esta na LinkedList
        if prev_node is None:
            print("Invalid")
            return
        # Cria-se um novo No e armazena-se o valor desejado.
        temp = Node(value)
        # O proximo no do recem criado vai ser o proximo original do existente.
        temp.next = prev_node.next
        # Muda-se o proximo do no existente para o No recem criado.
        prev_node.next = temp

    # Este Metodo Insere um elemento no final da LinkedList.
    def insertAtTheEnd(self, value):
        # Cria-se um novo No e armazena-se o valor desejado.
        temp = Node(value)
        # Se a LinkedList esta vazia,entao o novo No passa a ser a head.
        if self.head is None:
            self.head = temp
            return
        # Vamos percorrer a LinkedList ate achar o ultimo elemento.
        last = self.head
        while last.next is not None:
            last = last.next
        # Achado o ultimo elemento,associamos o novo no como o proximo do ultimo elemento.
        last.next = temp

    # Metodo para printar uma LinkedList
    def printLinkedList(self):
        # Referencia para cabeca.
        temp = self.head
        # Percorremos toda a lista e vamos printando os elementos.
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Metodo para remover um certo elemento dado o valor.
    def deleteElementByValue(self, value):
        # Teste para ver se a Lista nao esta vazia.
        if self.head is None:
            print("Lista Vazia")
            return
        else:
            # Se a head for o elemento para excluir,a head passa a ser o next da head original.
            if self.head.value == value:
                self.head = self.head.next
                return
            else:
                # Percorre-se a lista ate encontrar o No interior ao que se quer excluir.
                temp = self.head
                while temp.next.value is not value:
                    temp = temp.next
                # Excluimos o no exato tirando a referencia do anterior a ele,fazendo apontar a
                # referencia do anterior ao proximo elemento do elemento que queremos remover.
                temp.next = temp.next.next


if __name__ == '__main__':
    my_list = LinkedList()
    my_list2 = LinkedList()
    my_list.insertAtBeginning(10)
    my_list.insertAtBeginning(12)
    my_list.insertAtBeginning(102)
    my_list.insertAtTheEnd(1000)
    my_list.insertAfterGivenNode(my_list.head, 1)
    my_list.printLinkedList()
    print("----------")
    my_list.deleteElementByValue(102)
    my_list.printLinkedList()
