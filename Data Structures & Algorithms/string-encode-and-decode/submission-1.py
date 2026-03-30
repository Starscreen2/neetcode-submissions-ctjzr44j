class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            i = j + 1
            decoded_string = s[i:i+length]
            decoded_strings.append(decoded_string)
            i += length
        return decoded_strings

