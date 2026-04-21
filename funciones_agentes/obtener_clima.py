from selenium.webdriver.common.by import By
import time

def obtener_clima(consulta, driver):
    driver.get(f"https://www.google.com/search?q={consulta}")
    time.sleep(3) 
    try:
        # Selectores estándar del widget de clima de Google
        temp = driver.find_element(By.ID, "wob_tm").text
        desc = driver.find_element(By.ID, "wob_dc").text
        return f"El clima actual es de {temp}°C con {desc}."
    except:
        return "No se pudo cargar el widget del clima. Intenta: 'clima en Toluca'."
