
import re
import urllib.request as urllib2

class AresReader:

    def __init__(self, ic, language = 'cz') -> None:
        self.link = 'https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_res.cgi'
        self.ic = ic
        self.language = language

    def file_get_contents(self):
        url = self.link + "?ico=" + self.ic + "&jazyk=" + self.language + "&xml=1"
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers = hdr)
        try:
            page = urllib2.urlopen(req)
            return page.read().decode("utf-8")
        except:
            return ""
        
    def printAres(self):
        data = self.file_get_contents()
        tag = ['ICO', 'OF', 'N', 'NU', 'CD', 'PSC', 'NPF', 'Nazev_NACE', 'KPP', 'Zuj_kod_orig', 'NZUJ']
        out = {}

        for t in tag :
            regex = r"<D:" + t + ">(.*?)<\/D"
            for match in re.finditer(regex, str(data), re.MULTILINE):
                val = match.group(1)
                out[t] = val

        return out
