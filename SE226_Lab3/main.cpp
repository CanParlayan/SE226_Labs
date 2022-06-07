#include <iostream>
using namespace std;
#define MAX 4

class Node {
public:
    int data;
    Node *next;
    Node(int x, Node *n) {
        data = x;
        next = n;
    }
};

class Stack {
private:Node *top;
private:int s;
public:
    Stack () {
        top = nullpointer;
        s = 0;
    };

    bool push(int data) {
        if (s == MAX) {
            cout << "Stack overflow!" << endl;
        } else if (top == nullpointer) {
            top = new Node(data, nullpointer);
            s++;
            cout << "First data has been added!" << endl;
        } else {
            Node *n = new Node(data, top);
            top = n;
            s++;
            cout << "New data has been added on previous data!" << endl;
        }
    }

    bool isEmpty() {
        if(top == NULL) {
            return true;
        } else {
            return false;
        }
    }

    Node* pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
        } else {
            Node *temp;
            temp = top;
            top=top->next;
            s--;
            cout << "Data has been deleted!" << endl;
            return temp;
        }
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
        } else {
            return top->data;
        }
    }

    int size () {
        return s;
    }
};

int main() {
    class Stack s;
    cout << "Is the stack empty? " << s.isEmpty() << endl;
    s.push(10);
    cout << "Data on the top: " << s.peek() << endl;
    s.push(20);
    cout << "Data on the top: " << s.peek() << endl;
    s.push(30);
    s.push(40);
    cout << "Size of stack: " << s.size() << endl;
    cout << "Data on the top: " << s.peek() << endl;
    cout << "Is the stack empty? " << s.isEmpty() << endl;
    s.pop();
    cout << "Size of stack: " << s.size() << endl;
    cout << "Data on the top: " << s.peek() << endl;

    return 0;
}
