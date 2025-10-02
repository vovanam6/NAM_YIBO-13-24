Бинарная куча
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    priority_queue<int, vector<int>, greater<int>> minHeap;

    minHeap.push(7);
    minHeap.push(2);
    minHeap.push(9);
    minHeap.push(1);
    minHeap.push(5);

    cout << "Минимальный элемент: " << minHeap.top() << endl;
    minHeap.pop();
    cout << "После удаления минимального: " << minHeap.top() << endl;

    return 0;
}

Куча Фибоначчи
#include <iostream>
using namespace std;

struct Node {
    int key, degree;
    Node *parent, *child, *left, *right;
    bool mark;
    Node(int val) {
        key = val;
        degree = 0;
        parent = child = nullptr;
        left = right = this;
        mark = false;
    }
};

int main() {
    Node* node = new Node(10);
    cout << "Создан узел кучи Фибоначчи с ключом: " << node->key << endl;
    return 0;
}

Хеш-таблица
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> hashTable;

    hashTable["Alice"] = 25;
    hashTable["Bob"] = 30;

    cout << "Alice: " << hashTable["Alice"] << endl;
    cout << "Bob: " << hashTable["Bob"] << endl;

    return 0;
}

Биномиальная куча
#include <iostream>
using namespace std;

struct Node {
    int key, degree;
    Node* parent;
    Node* child;
    Node* sibling;
    Node(int val) {
        key = val;
        degree = 0;
        parent = child = sibling = nullptr;
    }
};

class BinomialHeap {
public:
    Node* mergeTrees(Node* b1, Node* b2) {
        if (b1->key > b2->key)
            swap(b1, b2);
        b2->parent = b1;
        b2->sibling = b1->child;
        b1->child = b2;
        b1->degree++;
        return b1;
    }
};

int main() {
    Node* n1 = new Node(10);
    Node* n2 = new Node(20);
    BinomialHeap bh;
    Node* root = bh.mergeTrees(n1, n2);
    cout << "Корень после слияния: " << root->key << endl;
    return 0;
}
