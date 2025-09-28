#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX = 100;

class Stack
{
private:
    int stack[MAX], size = 0;

public:
    Stack(int n)
    {
        for (int i = 0; i < n; i++)
        {
            stack[i] = rand() % 90 + 10;
        }
        size = n;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << stack[i] << " ";
        }
        cout << "\n\n";
    }

    void push(int x)
    {
        if (size == MAX)
        {
            cout << "Stack is full\n\n";
        }
        else
        {
            stack[size++] = x;
            cout << "Element is added\n\n";
        }
    }

    void pop()
    {
        if (size == 0)
        {
            cout << "Stack is Empty\n\n";
        }
        else
        {
            size--;
            cout << "Last Element is deleted\n\n";
        }
    }

    int last()
    {
        return stack[size - 1];
    }

    bool isEmpty()
    {
        return size == 0;
    }
};

void print_menu()
{
    cout << "1 - Print Stack\n";
    cout << "2 - Add Element\n";
    cout << "3 - Delete last Element\n";
    cout << "4 - Print last Element\n";
    cout << "5 - Check size\n";
    cout << "0 - Exit\n";
    cout << "Enter your choise: ";
}

int main()
{
    srand(time(NULL));
    Stack s(10);
    for (;;)
    {
        print_menu();
        int k;
        cin >> k;

        switch (k)
        {
        case 1:
            s.print();
            break;

        case 2:
            int x;
            cout << "Enter x: ";
            cin >> x;
            s.push(x);
            break;

        case 3:
            s.pop();
            break;

        case 4:
            cout << "Last Element:" << s.last()
                 << endl
                 << endl;
            break;

        case 5:
            s.isEmpty() ? cout << "Stack is Empty\n\n" : cout << "Stack is'n Empty\n\n";
            break;

        case 0:
            return 0;
            break;

        default:
            cout << "Wrong choise\n\n";
            break;
        }
    }
}