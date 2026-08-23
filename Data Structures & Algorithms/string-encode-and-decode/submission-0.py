class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = []
        for ch in strs:
            length = len(ch)
            piece = str(length) + "#" + ch
            encoded_parts.append(piece)
        
        return "".join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        decoded_parts = []
        i = 0
        while i < len(s):
            # i 부터 시작해서 # 이 어디에 있는지 찾기
            j = s.find("#", i)

            # i 부터 j 직전까지가 length
            length = int(s[i:j])

            word = s[j+1:j+1+length]
            decoded_parts.append(word)

            i = j + 1 + length

        return decoded_parts

