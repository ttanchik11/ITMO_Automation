class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
search = Input('input#search', "поиск")

#home_two = ButtonTwo('Домой', r'\home', 'button#home')
button = Input('input#button', 'батон')
title = Input('input#title', 'название')
link = Input('input#link', 'ссылка')

print(search.loc, search.text, button.loc, button.text, title.loc, title.text, link.loc, link.text,)
#ответ  - input#search поиск input#button батон input#title название input#link ссылка

class Page:
    def __init__(self, url):
        self.url = url
    def get_url(self):
        print(self.url)
home = Page("https://example.com")
home.get_url()