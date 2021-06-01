import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(URL): 
    ''' 
    A function that takes in a url and returns an integer
    Counts how many 'citation needed' in the article. 
    '''

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    citation_needed=[]
    for par in results:
        try:
            all_para = par.find_all('span', string = lambda text: 'citation' in text.lower())
            if all_para :
                for i in range(len(all_para)): 
                    citation_needed.append(all_para[i])
        except Exception as e:
            continue
    return len(citation_needed)

def get_citations_needed_report(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    all_paragraphs  = []
    all_lines = []

    resultsss = results.find_all('p')
    for i in resultsss:
        try:
            all_para = i.find_all('span', string = lambda text: 'citation' in text.lower())
            if all_para:
                for j in range(len(all_para)):

                    all_paragraphs.append(i.text) 

                    pos = i.text.index('citation') 
                    line = i.text[:pos-1].split(". ")
                    all_lines.append(line[-1])

                        
        except Exception as e:
            continue

    output = ''
    for p in range(len(all_paragraphs)):
        output += f'citation {p+1}: \n'
        output += f'paragraph: {all_paragraphs[p]} \n'
        # output += f'{all_lines[p]} \n\n\n'

    f = open("citation.txt", "w")
    f.write(output)
    f.close()

    return output 


if __name__ == "__main__":

    print(get_citations_needed_report(URL))
    print(get_citations_needed_count(URL))


