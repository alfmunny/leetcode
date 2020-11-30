class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2: return len(chars)
        
        read, write = 1, 0
        count = 1
        
        while read < len(chars):
            if chars[read] == chars[read-1]:
                count += 1
            elif count > 1:
                chars[write] = chars[read-1]
                for s in list(str(count)):
                    write += 1
                    chars[write] = s
                write += 1
                count = 1
            else:
                chars[write] = chars[read-1]
                write += 1        
            read += 1
            
        if count == 1:
            chars[write] = chars[read-1]
            write += 1
        else:
            chars[write] = chars[read-1]
            for s in list(str(count)):
                write += 1
                chars[write] = s
            write += 1
            
        return write
