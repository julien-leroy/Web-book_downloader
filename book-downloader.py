import urllib

def save_book(filename, url):
    f = open(filename, 'wb')
    jpg = urllib.urlopen(url)
    f.write(jpg.read())
    f.close()

def save_books():
    url = "https://images.yumpu.com/yumpu.com/000/022/992/091/1394164173_1163/zoom/COBIT_5_Enabling_Processe{}.jpg?v=4441"
    filename = "CobiT 5 Enabling Processes - {}.jpg"
    number = "{0:06d}"
    for i in range(230):
        formatted_number = number.format(i)
        save_book(filename.format(formatted_number), url.format(formatted_number))

save_books()
