from typing import *
from template.problem import Problem

class Partition:
    def __init__(self, id, idx, n):
        self.id = id
        self.idx = idx
        self.n = n
        self.next = None
        self.prev = None
    def __str__(self):
        return f"({self.id},{self.idx},{self.n})"
    def __repr__(self):
        return f"({self.id},{self.idx},{self.n})"

class DoublyLinkedList:
    """Lista doblemente enlazada con referencias a head y tail."""
    def __init__(self, iterable=None):
        self.head: Optional[Partition] = None
        self.tail: Optional[Partition] = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0
    
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(x) for x in self) + "]"

    # Append al final (O(1))
    def append(self, newNode: Partition) -> Partition:
        if self.tail is None:  # lista vacía
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self._size += 1
        return newNode

    # Insertar después de un nodo dado (O(1))
    def insert_after(self, ref_node: Partition, newNode: Partition) -> Partition:
        if ref_node is None:
            raise ValueError("ref_node no puede ser None")
        newNode.prev = ref_node
        newNode.next = ref_node.next
        ref_node.next = newNode
        if newNode.next:
            newNode.next.prev = newNode
        else:  # ref_node era tail
            self.tail = newNode
        self._size += 1
        return newNode
    
    def getPartitionIdFromNode(self, ref_node: Partition, partitionId: int):
        while partitionId != ref_node.id:
            ref_node = ref_node.prev
            if ref_node is None:
                return None
        return ref_node
    
    # Iteradores
    def __iter__(self) -> Iterator[Partition]:
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def iter_nodes(self) -> Iterator[Partition]:
        cur = self.head
        while cur:
            yield cur
            cur = cur.next


class Day09(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def part1(self):
        disk = [int(x) for x in list(self.input[0])]
        translation = []
        id = 0
        for i in range(0, len(disk), 2):
            a = 0
            for _ in range(disk[i]):
                translation.append(id)
            if i == len(disk) - 1:
                break
            for _ in range(disk[i+1]):
                translation.append(None)
            id+=1
        # Rearrange
        i = 0
        j = len(translation) - 1

        while i < j:
            while translation[j] is None:
                j-=1
            if translation[i] is None:
                translation[i], translation[j] = translation[j], translation[i]
                j -= 1
            i += 1
        i = 0
        total = 0
        while translation[i] is not None:
            total += i * translation[i]
            i+=1
        return total


    def getDecodedPartitions(self, partitions: list[Partition]):
        text = ""
        idx = 0
        for p in partitions:
            if p.idx != idx:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
            for i in range(p.n):
                text += '.' if p.id is None else str(p.id)
                idx += 1
        return text

    def part2(self):
        disk = [int(x) for x in list(self.input[0])]
        # print(disk)
        # (id, i, len)
        id = 0
        idx = 0
        partitions = DoublyLinkedList()
        for b in range(len(disk)):
            n = disk[b]
            partition = Partition(id if b % 2 == 0 else None, idx, n)
            if n > 0:
                partitions.append(partition)
            idx += n
            if b % 2 == 0:
                id+=1

        processedPartition = partitions.tail
        processedId = processedPartition.id
        
        while processedId > 0:
            # Procesamos el actual
            replaceNode = partitions.head
            while replaceNode.idx < processedPartition.idx:
                if replaceNode.id is not None or processedPartition.n > replaceNode.n:
                    replaceNode = replaceNode.next
                    continue
                diff = replaceNode.n - processedPartition.n
                replaceNode.id = processedPartition.id
                replaceNode.n = processedPartition.n
                processedPartition.id = None
                if diff > 0:
                    newPartition = Partition(None, replaceNode.idx + processedPartition.n, diff)
                    partitions.insert_after(replaceNode, newPartition)
                break                
            processedId -= 1
            processedPartition = partitions.getPartitionIdFromNode(processedPartition, processedId)
        
        total = 0
        idx = 0
        for p in partitions:
            for _ in range(p.n):
                if p.id is not None:
                    total += p.id * idx
                idx += 1
        return total
