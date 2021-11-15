import webbrowser
""" Ouvrir URL avec Python sans autre pluggin """





url = 'http://docs.python.org/'


# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


webbrowser.get(chrome_path).open(url)

webbrowser.open_new("https://ts1.travian.fr/build.php?t=5&id=32")