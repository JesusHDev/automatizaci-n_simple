from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obtener_precio_accion(consulta, driver):
    # Limpiamos el ticker
    query = consulta.lower().replace("precio", "").replace("accion", "").replace("de", "").strip()
    url = f"https://finance.yahoo.com/quote/{query}"
    driver.get(url)
    
    # Tiempo para que el JavaScript de Yahoo "hidrate" los datos
    time.sleep(6) 
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # El selector más robusto de Yahoo para el precio principal
        selector = 'fin-streamer[data-field="regularMarketPrice"]'
        
        # Esperamos a que el elemento esté presente en el código (DOM)
        elemento = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        
        # --- EL GRAN TRUCO ---
        # .text a veces falla en headless. 
        # .get_attribute("textContent") extrae el valor directamente del motor,
        # sin importar si Selenium cree que es "invisible".
        precio = elemento.get_attribute("textContent").strip()
        
        if precio and any(char.isdigit() for char in precio):
            return f"El valor actual de {query.upper()} es de ${precio} USD."
        else:
            return "El elemento cargó pero el número sigue vacío. Reintenta en 5 segundos."

    except Exception as e:
        driver.save_screenshot("error_final_wsl.png")
        return "Error de extracción. Revisa la captura 'error_final_wsl.png'."
