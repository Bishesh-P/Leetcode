class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charMapping = {}

        for i in range(len(s)):
            original = s[i]
            replacement = t[i]

            if original not in charMapping:
                if replacement in charMapping.values():
                    return False

                charMapping[original] = replacement

            else:
                mappedCharacter = charMapping[original]

                if mappedCharacter != replacement:
                    return False

        return True