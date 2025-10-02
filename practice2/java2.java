Бинарная куча
import java.util.PriorityQueue;

public class BinaryHeapExample {
    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        minHeap.add(7);
        minHeap.add(2);
        minHeap.add(9);
        minHeap.add(1);
        minHeap.add(5);

        System.out.println("Минимальный элемент: " + minHeap.peek());
        minHeap.poll();
        System.out.println("После удаления: " + minHeap.peek());
    }
}

Куча Фибоначчи
class FibonacciHeapNode {
    int key, degree;
    FibonacciHeapNode parent, child, left, right;
    boolean mark;

    public FibonacciHeapNode(int key) {
        this.key = key;
        this.degree = 0;
        this.left = this.right = this;
        this.mark = false;
    }
}

public class FibonacciHeapDemo {
    public static void main(String[] args) {
        FibonacciHeapNode node = new FibonacciHeapNode(10);
        System.out.println("Создан узел кучи Фибоначчи с ключом: " + node.key);
    }
}

Хеш-таблица
import java.util.HashMap;

public class HashTableExample {
    public static void main(String[] args) {
        HashMap<String, Integer> hashTable = new HashMap<>();

        hashTable.put("Alice", 25);
        hashTable.put("Bob", 30);

        System.out.println("Alice: " + hashTable.get("Alice"));
        System.out.println("Bob: " + hashTable.get("Bob"));
    }
}

Биноминальная куча
class BinomialNode {
    int key, degree;
    BinomialNode parent, child, sibling;

    public BinomialNode(int key) {
        this.key = key;
        this.degree = 0;
        this.parent = this.child = this.sibling = null;
    }
}

class BinomialHeap {
    public BinomialNode merge(BinomialNode b1, BinomialNode b2) {
        if (b1.key > b2.key) {
            BinomialNode temp = b1;
            b1 = b2;
            b2 = temp;
        }
        b2.parent = b1;
        b2.sibling = b1.child;
        b1.child = b2;
        b1.degree++;
        return b1;
    }
}

public class BinomialHeapDemo {
    public static void main(String[] args) {
        BinomialNode n1 = new BinomialNode(10);
        BinomialNode n2 = new BinomialNode(20);
        BinomialHeap bh = new BinomialHeap();
        BinomialNode merged = bh.merge(n1, n2);
        System.out.println("Корень после слияния: " + merged.key);
    }
}
