from selenium.webdriver.common.by import By
import time

def obtener_clima(consulta, driver):
    """Busca el clima actual en Google"""
    driver.get(f"https://www.google.com/search?q={consulta}")
    time.sleep(2) 
    try:
        temperatura = driver.find_element(By.CSS_SELECTOR, "#wob_tm").text
        descripcion = driver.find_element(By.CSS_SELECTOR, "#wob_dc").text
        return f"El clima para tu búsqueda es: {temperatura}°C, {descripcion}."
    except:
        return "No pude obtener los datos del clima."
