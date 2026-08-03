class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):
            # Skip if character is already in the stack
            if ch in seen:
                continue

            # Remove larger characters if they appear later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                seen.remove(stack.pop())

            # Add current character
            stack.append(ch)
            seen.add(ch)

        return "".join(stack)