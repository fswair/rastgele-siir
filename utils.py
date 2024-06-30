import requests, bs4

class Poet:
    endpoint: str
    name: str
    def __init__(self, endpoint: str, name: str):
        self.endpoint = endpoint
        self.name = name
    @property
    def url(self):
        return f"https://www.antoloji.com{self.endpoint}"
    
    def __str__(self):
        return self.name
    
class Poem:
    endpoint: str
    title: str
    poem: str
    poet: str
    def __init__(self, endpoint: str, title: str, poem: str, poet: Poet):
        self.endpoint = endpoint
        self.title = title
        self.poem = poem
        self.poet = poet
    @property
    def url(self):
        return f"https://www.antoloji.com{self.endpoint}"
    
    def __str__(self):
        return f"{self.title} - {self.poet}"



class Antoloji:
    def get_poet(self, poet: str):
        url = f"https://www.antoloji.com/arama-detay/?yer=1&arama={poet}"
        req = requests.get(url)
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        poet = soup.select_one(".list-col-1").select_one("a")
        endpoint = poet["href"]
        return endpoint

    def get_poems_of_poet(self, poet_endpoint: str = "/mert-sirakaya/"):
        poems = []
        for i in range(1, 100):
            url = f"https://www.antoloji.com/{poet_endpoint}/siirleri/ara-/sirala-/sayfa-{i}/"
            req = requests.get(url)
            soup = bs4.BeautifulSoup(req.text, "html.parser")
            poemlist = soup.select_one("div.poemListBox").select("li")
            if req.status_code != 200 or f"sayfa-{i-1}" in req.url:
                    print("there was no such page after", i - 1)
                    break
            for poem in poemlist:
                url = "https://antoloji.com" + poem.select_one("a")["href"]
                req = requests.get(url)
                content = req.text
                parser = bs4.BeautifulSoup(content, "html.parser")
                title = parser.select_one(".pd-title-a").text
                poem = parser.select_one(".pd-text")
                poem = '<br><br>'.join(map(lambda p: p.text.replace("\n", "<br>"), poem.select("p")))
                poems.append({"title": title.strip().lower(), "poem": poem.lower(), "url": req.url})
        return poems
    
    def get_poems(self, poem: str, page: int = 1):
        poems = []
        url = f"https://antoloji.com/arama-detay/sayfa-{page}/?yer=2&arama={poem}"
        req = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        poemlist = soup.select_one("div.list-content-full")
        if poemlist is None:
            return []
        poemlist = poemlist.select("li")
        for poem in poemlist[::-1]:
            print(poem)
            poemcursor = poem.select_one(".list-col-1").select_one("a")
            poetcursor = poem.select_one(".list-col-2").select_one("a")
            date = poem.select_one(".list-col-3").text.strip()
            url = "https://antoloji.com" + poemcursor["href"]
            title = poemcursor.text.strip()
            
            poeturl = "https://antoloji.com" + poetcursor["href"]
            poet = poetcursor.text.strip()
            poems.append({"title": title, "url": url, "poet": poet, "poet_url": poeturl, "date": date})
        return poems
    
    def get_poem(self, endpoint: str):
        import requests
        url = f"https://www.antoloji.com/{endpoint}"
        headers = {
            "Host": "www.antoloji.com",
            "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Accept-Language": "tr-TR",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

        response = requests.get(url, headers=headers)
        url = response.url
        
        bs = bs4.BeautifulSoup(response.text, "html.parser")
        title = bs.select_one(".pd-title-a")
        if title is None:
            return -1
        title = title.text
        urls = bs.select_one(".pd-detail")
        filtered = filter(lambda a: a["href"].endswith("yorumlari/") ,urls.select("a"))
        url = next(filtered)["href"].replace("/yorumlari/", "")
        title = bs.select_one(".pd-title-a").text
        poem = bs.select_one(".pd-text")
        poem = '<br><br>'.join(map(lambda p: p.text.replace("\n", "<br>"), poem.select("p")))
        poet = bs.select_one(".pb-title")
        poet_name = poet.text.strip().lower()
        poet_url = poet.select_one("a")["href"]
        return Poem(
            title=title.strip().lower(),
            poem=poem.lower(),
            endpoint=url,
            poet=Poet(
                endpoint=poet_url,
                name=poet_name
            )
        )
    
    def get_random_poem(self):
        import requests
        url = "https://www.antoloji.com/siir/rastgele"
        headers = {
            "Host": "www.antoloji.com",
            "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Accept-Language": "tr-TR",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

        response = requests.get(url, headers=headers)
        url = response.url
        
        bs = bs4.BeautifulSoup(response.text, "html.parser")
        title = bs.select_one(".pd-title-a").text
        urls = bs.select_one(".pd-detail")
        filtered = filter(lambda a: a["href"].endswith("yorumlari/") ,urls.select("a"))
        url = next(filtered)["href"].replace("/yorumlari/", "")
        title = bs.select_one(".pd-title-a").text
        poem = bs.select_one(".pd-text")
        poem = '<br><br>'.join(map(lambda p: p.text.replace("\n", "<br>"), poem.select("p")))
        poet = bs.select_one(".pb-title")
        poet_name = poet.text.strip().lower()
        poet_url = poet.select_one("a")["href"]
        return Poem(
            title=title.strip().lower(),
            poem=poem.lower(),
            endpoint=url,
            poet=Poet(
                endpoint=poet_url,
                name=poet_name
            )
        )