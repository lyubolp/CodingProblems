class Codec:
    def __init__(self):
        self.urls = {}
        self.ids = 0
        self.base = 'http://tinyurl.com/'
        
    def __encode(self) -> str:
        self.ids += 1
        return hex(self.ids)
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tiny_url = self.base + self.__encode()
        
        self.urls[tiny_url] = longUrl
        return tiny_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

