#include "ransom_note.h"

bool Solution::canConstruct(string ransomNote, string magazine)
{
    unordered_map<char, int> r_map;
    unordered_map<char, int> m_map;
    
    for(char c : ransomNote)
    {
        if(r_map.count(c) == 0) r_map[c] = 1;
        else r_map[c]++;
    }

    for(char c : magazine)
    {
        if(m_map.count(c) == 0) m_map[c] = 1;
        else m_map[c]++;
    }
    
    for(auto const& x: r_map)
    {
        
        if(m_map.count(x.first)) return false;
        //else if(m_map[x.first] < x.second) return false;
    }
    return true;
}
