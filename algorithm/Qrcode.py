#Biblioteca disponível em 'https://pypi.org/project/qrcode/'
import qrcode

img = qrcode.make(input("Link>"))
#A linha abaixo verifica o tipo do objeto criado
type(img)  # qrcode.image.pil.PilImage
img.save(f"{input("Nome>")}.png")