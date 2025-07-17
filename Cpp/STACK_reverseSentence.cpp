#include <iostream>
using namespace std;
#include <stack>

void reverseSentence(string s)
{
    stack<string> rs; // stack for storing different words
    for (int i = 0; i < s.length(); i++)
    {
        string word = ""; // string to store each word
        while (s[i] != ' ' && i < s.length())
        {
            // if(i==s.length())
            //     break;
            word += s[i];
            i++;
        }
        rs.push(word);
    }

    while (!rs.empty())
    {
        cout << rs.top() << " ";
        rs.pop();
    }
}
int main()
{
    string s = "Hello, how are you?";
    reverseSentence(s);
}