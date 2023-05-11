
def worm(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    response.encoding = "utf-8"
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    texts = soup.find_all(string=True)
    result = []
    for text in texts:
        if "\u4e00" <= text <= "\u9fff":  # 判断text是否是汉字
            result.append(text)

    print("".join(result))