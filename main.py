from requests_html import HTMLSession
from rake_nltk import Rake

import sys, getopt

def main(argv):
   url = ''
   keyword = ''
   try:
      opts, args = getopt.getopt(argv,"hu:k:",["url=","keyword="])
   except getopt.GetoptError:
      print('main.py -u <url> -k <keyword>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--help"):
         print('main.py -i <url> -o <keyword>')
         sys.exit()
      elif opt in ("-u", "--url"):
         url = arg
      elif opt in ("-k", "--keyword"):
         keyword = arg
   print(f'Analyzing web element matching "{keyword}" at {url}')

   # print(extract_text())

   # r = Rake()
   # # r = Rake(language='swedish')

   # r.extract_keywords_from_text(extract_text())
   # for rating, keyword in r.get_ranked_phrases_with_scores():
   #     if rating > 5:
   #         print(round(rating), keyword)


# English example
def extract_text():
    s = HTMLSession()
    url = 'https://career.odevo.com/jobs/1652504-linux-sys-admin'
    r = s.get(url)
    # Select an element with a CSS selector
    # return r.html.find('body > main > section > div.mx-auto.prose.font-company-body.overflow-hidden', first=True).text
    # Select an element with XPath
    # return r.html.xpath('/html/body/main/section[2]/div', first=True).text
    # Select an element with search
    return r.html.find('div', containing='Zabbix', first=True).text


if __name__ == "__main__":
   main(sys.argv[1:])

