#include "word_pattern.h"
#include <vector>
#include <map>
#include <iostream>


bool WordPattern::wordPattern(std::string pattern, std::string str)
{
        std::vector<std::string> words = splitWords(str);
        std::map<char, std::string> dict;
        std::map<std::string, char> rev_dict;
        
        if(words.size() != pattern.size())
            return false;
        else
        {
            for(int i = 0; i < pattern.size(); i++)
            {
                if(dict.count(pattern[i]) == 0 && rev_dict.count(words[i]) == 0)
                {
                    dict[pattern[i]] = words[i];
                    rev_dict[words[i]] =  pattern[i];
                }
                else
                {
                    if(dict[pattern[i]] != words[i] || rev_dict[words[i]] != pattern[i])
                        return false;
                    else
                        continue;
                }
            }
        }
        return true;
}

std::vector<std::string> WordPattern::splitWords(std::string str)
{
        std::string word = "";
        std::vector<std::string> words;
        for(int i = 0; i < str.size() + 1; i++)
        {
            if (str[i] == char(' ') || str[i] == char('\0'))
            {
                words.push_back(word);
                word = "";
            }
            else
            {
                word.push_back(str[i]);
            }
        }
        return words;
}
