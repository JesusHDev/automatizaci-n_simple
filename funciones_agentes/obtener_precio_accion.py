from selenium.webdriver.common.by import By
import time

def obtener_precio_accion(consulta, driver):
    driver.get(f"https://www.google.com/search?q={consulta}")
    time.sleep(3) # Damos 3 segundos para que cargue en WSL
    try:
        # Selectores más genéricos que Google usa para finanzas
        empresa = driver.find_element(By.CSS_SELECTOR, "div.PZPpjf").text
        # Buscamos el precio por el atributo jsname que es más estable
        precio = driver.find_element(By.CSS_SELECTOR, 'span[jsname="vL77Mc"]').text
        return f"La empresa {empresa} cotiza actualmente en {precio}."
    except:
        return "No pude encontrar el precio. Intenta con 'precio accion Apple'."
