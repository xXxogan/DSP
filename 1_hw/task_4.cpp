#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX = 100;

class Array
{
private:
    int array[MAX], size = 0;

public:
    Array(int n)
    {
        for (int i = 0; i < n; i++)
        {
            array[i] = rand() % 90 + 10;
        }
        size = n;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << array[i] << " ";
        }
        cout << "\n\n";
    }

    void add(int x)
    {
        bool flag = false;

        for (int i = 0; i < size; i++)
        {
            if (array[i] == x)
            {
                flag = true;
            }
        }

        if (flag == false)
        {
            if (size == MAX)
            {
                cout << "Array is full\n\n";
            }
            else
            {
                array[size++] = x;
                cout << "Element is added\n\n";
            }
        }
        else
        {
            cout << "Element is alredy in array\n\n";
        }
    }

    void deleteElement(int value)
    {
        bool flag = false;
        int a = -1;

        for (int i = 0; i < size; i++)
        {
            if (array[i] == value)
            {
                flag = true;
                a = i;
            }
        }

        if (flag == false)
        {
            cout << "Array doesn't containts the Element\n\n";
        }
        else
        {
            for (int i = a; i < size; i++)
            {
                array[i] = array[i + 1];
            }
            size--;

            cout << "Element is deleted\n\n";
        }
    }

    void containts(int x)
    {
        bool flag = false;

        for (int i = 0; i < size; i++)
        {
            if (array[i] == x)
            {
                flag = true;
            }
        }

        if (flag == false)
        {
            cout << "Array doesn't containts the Element\n\n";
        }
        else
        {
            cout << "Array containts the Element\n\n";
        }
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
    cout << "3 - Delete Element by value\n";
    cout << "4 - Does the Array containts a value\n";
    cout << "5 - Check size\n";
    cout << "0 - Exit\n";
    cout << "\nEnter your choise: ";
}

int main()
{
    srand(time(NULL));
    Array s(10);
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
            cout << "Enter Element: ";
            cin >> x;
            s.add(x);
            break;

        case 3:
            int v;
            cout << "Enter value: ";
            cin >> v;
            s.deleteElement(v);
            break;

        case 4:
            int e;
            cout << "Enter element: ";
            cin >> e;
            s.containts(e);
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