#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX = 100;

class Queue
{
private:
    int queue[MAX], size = 0;

public:
    Queue(int n)
    {
        for (int i = 0; i < n; i++)
        {
            queue[i] = rand() % 90 + 10;
        }
        size = n;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << queue[i] << " ";
        }
        cout << "\n\n";
    }

    void enqueue(int x)
    {
        if (size == MAX)
        {
            cout << "Queue is full\n\n";
        }
        else
        {
            queue[size++] = x;
            cout << "Element is added\n\n";
        }
    }

    void dequeue()
    {
        size--;

        for (int i = 0; i < size; i++)
        {
            queue[i] = queue[i + 1];
        }
    }

    int first()
    {
        return queue[0];
    }

    bool isEmpty()
    {
        return size == 0;
    }
};

void print_menu()
{
    cout << "1 - Print Queue\n";
    cout << "2 - Add Element\n";
    cout << "3 - Delete first Element\n";
    cout << "4 - Print first Element\n";
    cout << "5 - Check size\n";
    cout << "0 - Exit\n";
    cout << "\nEnter your choise: ";
}

int main()
{
    srand(time(NULL));
    Queue s(10);
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
            s.enqueue(x);
            break;

        case 3:
            s.dequeue();
            break;

        case 4:
            cout << "First Element:" << s.first()
                 << endl
                 << endl;
            break;

        case 5:
            s.isEmpty() ? cout << "Queue is Empty\n\n" : cout << "Queue is'n Empty\n\n";
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