class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_p = ['(', '{', '[']
        close_p = [')', '}', ']']
        # Stack
        stack = []
        for elm in s:
            # if opening bracket
            if elm in open_p:
                # Add the element to the stack
                stack.append(elm)

            else:

                # if the stack is empty
                if len(stack) == 0:
                    return False

                    # Pop the element off the stack
                poped = stack.pop()

                # if the indexes are the same
                if open_p.index(poped) != close_p.index(elm):
                    return False

        return len(stack) == 0


class Solution2:
    def isValid(self, s):
        stack = []
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for x in s:
            if x in map:
                stack.append(map[x])
            else:
                if len(stack) != 0:
                    top_element = stack.pop()
                    if x != top_element:
                        return False
                    else:
                        continue
                else:
                    return False
        return len(stack) == 0
