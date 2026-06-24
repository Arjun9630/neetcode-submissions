class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for strr in strs:
            for char in strr:
                asci = ord(char)
                encoded_asci = (asci+6)%255
                encoded_str += chr(encoded_asci)
            encoded_str += " "
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = ""
        decoded_str_list = []
        for chrr in s:
            if chrr == " ":
                decoded_str_list.append(decoded_str)
                decoded_str = ""
                continue
            asci = ord(chrr)
            decoded_asci = (asci-6)%255
            decoded_str += chr(decoded_asci)
        return decoded_str_list