from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from utils import sanitizar

# Configuración de Selenium en modo invisible
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input:
        return obtener_precio_accion
    return None

print("Asistente Virtual Activo. ¿En qué puedo ayudarte?")
try:
    while True:
        prompt = input("---> ")
        user_input = sanitizar(prompt)
        
        if user_input in ["salir", "exit", "quit"]:
            print("Cerrando sesión...")
            break
            
        agente = procesar_input(user_input)
        if agente:
            print(f"Respuesta: {agente(user_input, driver)}")
        else:
            print("Por favor, pregunta por el clima o una acción.")
finally:
    driver.quit()
