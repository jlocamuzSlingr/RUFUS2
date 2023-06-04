import re
import pytesseract
import cv2
import requests

from .texto_a_ingred import procesar_oracion

def obtener_texto_imagen(menu_object):
    url_imagen = menu_object['image']
    url_imagen_sin_host = url_imagen.replace('http://192.168.1.42:8000/', '')
    img = cv2.imread(url_imagen_sin_host)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    texto = pytesseract.image_to_string(img, lang='spa')
    print(texto)
    oraciones = re.split(r'\$\d+', texto)
    print(oraciones)
    texto = [linea.lower().replace('\n', '').rstrip() for linea in oraciones if linea.strip()]
    print(texto)
    palabras_oraciones = []
    for oracion in texto:
        oracion = oracion.split('$')[0].strip()
        
        palabras_oraciones.append(procesar_oracion(oracion))
    #print("palabras oraciones ", palabras_oraciones)
    #[['milanesa de cerdo', 'papas fritas'], ['pancho', 'nuggets'], ['hamburguesa', 'fritas']]
    return texto, palabras_oraciones
