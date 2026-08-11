class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        i = 0
        n = len(s)
        
        while i < n:
            startIndex = i
            endIndex = s.rfind(s[i])

            # Expand the partition if needed
            j = startIndex + 1
            while j <= endIndex:
                lastIndexOfNextChar = s.rfind(s[j])
                if lastIndexOfNextChar > endIndex:
                    endIndex = lastIndexOfNextChar
                j += 1
            
            partitions.append(endIndex - startIndex + 1)
            i = endIndex + 1          # jump to the next partition
        
        return partitions