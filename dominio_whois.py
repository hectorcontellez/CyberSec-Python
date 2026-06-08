import whois
# Importamos la función del script anterior (asegúrate de que el archivo se llame validacion_dominio.py)
from validacion_dominio import esta_registrado 

# ==============================================================================
# Descripción del Programa:
# Este script extrae información detallada de la base de datos WHOIS para un 
# dominio específico. Muestra datos críticos en la fase de recolección de 
# información (Information Gathering) como el registrador del dominio, 
# el servidor WHOIS, y las fechas de creación y expiración. 
# ==============================================================================

nombre_dominio = "google.com"

# Primero verificamos si el dominio está registrado usando nuestra función
if esta_registrado(nombre_dominio):
    # Obtenemos toda la información WHOIS del dominio
    info_whois = whois.whois(nombre_dominio)

    # Imprimimos el registrador (la empresa que gestiona la reserva del dominio, ej. GoDaddy, Namecheap)
    print("Registrador del dominio:", info_whois.registrar)

    # Imprimimos el servidor WHOIS
    print("Servidor WHOIS:", info_whois.whois_server)

    # Obtenemos e imprimimos la fecha de creación del dominio
    print("Fecha de creación del dominio:", info_whois.creation_date)

    # Obtenemos e imprimimos la fecha de expiración del dominio
    print("Fecha de expiración:", info_whois.expiration_date)

    # Imprimimos toda la información restante en bruto
    print("\n--- Información Completa WHOIS ---")
    print(info_whois)
