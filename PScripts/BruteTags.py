import requests
from bs4 import BeautifulSoup
import pandas as pd
from flair.data import Sentence
from flair.models import MultiTagger
from flair.tokenization import SciSpacyTokenizer

scp = SciSpacyTokenizer()
tagger = MultiTagger.load("hunflair")

def scrape_spl_indications(spl: str):
    xml = requests.get("https://www.accessdata.fda.gov/spl/data/{}/{}.xml".format(spl, spl)).content
    soup = BeautifulSoup(xml, 'xml')

    sections = soup.find_all("section")
    for i in sections : 
        if i.find("code", code="34067-9", codeSystem="2.16.840.1.113883.6.1") :
            return i.find("highlight").find("text").text

    return ""

s = set({})
spls = list(pd.read_csv("SPLS.csv")["SPL"])
for spl in spls :
    sentence = Sentence(spl,use_tokenizer=scp)
    tagger.predict(sentence)
    for i, e in enumerate(sentence.get_spans()):
        s.add((e.token, e.tag))
    print("Processed : ", spl)

df = pd.DataFrame(list(s))
df.columns = ["token", "tag"]
df.to_csv("Token_2_Tags.csv", index=False)
