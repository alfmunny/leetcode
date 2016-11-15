#include <string>
#include <stack>
#include <map>

class ValidParentheses
{
    bool isValid(std::string s) {
        std::stack<int> stack_s;

        for (int i = 0; i < s.size(); ++i)
        {
            switch(s[i])
            {
                case '(':
                case '{':
                case '[': stack_s.push(s[i]); break;
                case ')': if(stack_s.empty() || stack_s.top() != '(') return false; else stack_s.pop(); break;
                case '}': if(stack_s.empty() || stack_s.top() != '{') return false; else stack_s.pop(); break;
                case ']': if(stack_s.empty() || stack_s.top() != '[') return false; else stack_s.pop(); break;
            }
        }
        return stack_s.size() == 0 ? true : false;
    }
};