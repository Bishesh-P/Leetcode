class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = []

        k = 0

        for ch in s:

            # Build the number
            if ch.isdigit():
                k = k * 10 + int(ch)

            elif ch == '[':
                num_stack.append(k)
                k = 0
                string_stack.append('[')

            elif ch != ']':
                string_stack.append(ch)

            else:
                # Get everything inside [...]
                temp = ""

                while string_stack[-1] != '[':
                    temp = string_stack.pop() + temp

                # Remove '['
                string_stack.pop()

                # Get repetition count
                count = num_stack.pop()

                # Repeat the string
                temp = temp * count

                # Put decoded string back
                string_stack.append(temp)

        return ''.join(string_stack)