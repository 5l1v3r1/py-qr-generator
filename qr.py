import pyqrcode
#hayden
s = "http://technicalhayden.cf"
#haydem
url = pyqrcode.create(s)
#create
url.svg("myqr.svg", scale = 8)
