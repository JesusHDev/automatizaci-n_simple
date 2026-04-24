from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obtener_clima(consulta, driver):
    """Extrae el clima actual de Google usando esperas explícitas."""
    # Forzamos la búsqueda para que Google nos dé el widget de grados centígrados
    url = f"https://www.google.com/search?q={consulta.replace(' ', '+')}+centigrados"
    driver.get(url)
    
    # Espera técnica para carga en WSL
    time.sleep(3) 
    
    try:
        # Esperamos hasta 5 segundos a que aparezca el ID del clima
        wait = WebDriverWait(driver, 5)
        temp_element = wait.until(EC.presence_of_element_located((By.ID, "wob_tm")))
        
        temperatura = temp_element.text
        descripcion = driver.find_element(By.ID, "wob_dc").text
        ubicacion = driver.find_element(By.ID, "wob_loc").text
        
        return f"En {ubicacion} la temperatura es de {temperatura}°C con {descripcion}."
        
    except Exception:
        # Captura de pantalla para debug silencioso en tu carpeta del proyecto
        driver.save_screenshot("debug_clima.png")
        return "Google no mostró el widget de clima. Intenta ser más específico (ej. 'clima en Toluca')."
