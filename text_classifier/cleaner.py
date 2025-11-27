from bs4 import BeautifulSoup

class Cleaner():

    def __init__(self):
        pass 

    def replace_paragraph(self, text: str):
        return text.replace('</p>', '</p>\n')
    
    def remove_html_tags(self, text: str):
        return BeautifulSoup(text, 'lxml').text
    
    def clean(self, text: str):
        text = self.replace_paragraph(text)
        text = self.remove_html_tags(text)
        return text.strip()