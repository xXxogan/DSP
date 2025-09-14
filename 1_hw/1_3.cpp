#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX = 100;

class List
{
private:
    int list[MAX], size = 0;

public:
    List(int n)
    {
        for (int i = 0; i < n; i++)
        {
            list[i] = rand() % 90 + 10;
        }
        size = n;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << list[i] << " ";
        }
        cout << "\n\n";
    }

    void insert(int index, int x)
    {
        size++;

        for (int i = size; i > index; i--)
        {
            list[i] = list[i - 1];
        }

        list[index] = x;
    }

    void remove(int index)
    {
        for (int i = index; i < size; i++)
        {
            list[i] = list[i + 1];
        }

        size--;
    }

    int indexOf(int x)
    {
        for (int i = 0; i < size; i++)
        {
            if (list[i] == x)
            {
                return i;
            }
        }
        return -1;
    }

    bool isEmpty()
    {
        return size == 0;
    }
};

void print_menu()
{
    cout << "1 - Print Queue\n";
    cout << "2 - Insert Element by position\n";
    cout << "3 - Delete Element by position\n";
    cout << "4 - Index of Element\n";
    cout << "5 - Check size\n";
    cout << "0 - Exit\n";
    cout << "\nEnter your choise: ";
}

int main()
{
    srand(time(NULL));
    List s(10);
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
            int index;
            int x;
            cout << "Enter index: ";
            cin >> index;
            cout << "Enter x: ";
            cin >> x;
            s.insert(index, x);
            break;

        case 3:
            int i;
            cout << "Enter index: ";
            cin >> i;
            s.remove(i);
            break;

        case 4:
            int e;
            cout << "Enter element: ";
            cin >> e;
            cout << "Index of " << e << ": " << s.indexOf(e) << "\n\n";
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