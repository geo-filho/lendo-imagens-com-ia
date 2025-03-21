import cv2
import pytesseract

# Carregar a imagem
imagem = cv2.imread("inputs/exemplo.jpg")

# Converter para escala de cinza
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Extrair texto usando OCR
texto = pytesseract.image_to_string(gray, lang="por")

# Salvar o resultado em um arquivo
with open("output/resultado.txt", "w", encoding="utf-8") as f:
    f.write(texto)

print("Texto extraído salvo em output/resultado.txt!")
