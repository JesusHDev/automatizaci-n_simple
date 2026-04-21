from selenium.webdriver.common.by import By

def obtener_precio_accion(consulta, driver):
    """Busca precios en Google Finance usando selectores CSS"""
    driver.get(f"https://www.google.com/search?q={consulta}")
    try:
        # Selectores basados en tu inspección de navegador
        empresa = driver.find_element(By.CSS_SELECTOR, ".PZPpjf").text
        precio = driver.find_element(By.CSS_SELECTOR, "span[vL77Mc]").text
        ticker = driver.find_element(By.CSS_SELECTOR, ".Dbe7db").text
        return f"La empresa {empresa} ({ticker}) cotiza en {precio}."
    except:
        return "No se pudo encontrar el precio de la acción."
