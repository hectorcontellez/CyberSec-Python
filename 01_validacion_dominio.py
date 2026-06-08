import whois # Recuerda instalar la librería antes: pip install python-whois 

# ==============================================================================
# Descripción del Programa:
# Este script sirve para validar la existencia de un nombre de dominio en internet.
# Utiliza la herramienta WHOIS para consultar si el dominio está registrado.
# Es una excelente forma de verificar dominios antes de intentar extraer información
# más profunda durante la fase de recolección de información (Information Gathering).
# ==============================================================================

def esta_registrado(nombre_dominio): 
    """
    Función que devuelve un valor booleano (Verdadero/Falso) 
    indicando si el 'nombre_dominio' proporcionado se encuentra registrado.
    """ 
    try: 
        # Intentamos consultar la información del dominio usando la librería whois
        info_dominio = whois.whois(nombre_dominio) 
    except Exception: 
        # Si la consulta falla o lanza una excepción (ej. el dominio no existe), 
        # capturamos el error y devolvemos Falso.
        return False 
    else: 
        # Si la consulta fue exitosa, convertimos el nombre de dominio devuelto 
        # en la consulta a un valor booleano y lo retornamos (True).
        return bool(info_dominio.domain_name)

# Bloque principal de ejecución
if __name__ == "__main__": 
    
    # Prueba 1: Comprobando un dominio real y conocido
    print("¿El dominio 'google.com' está registrado?")
    print(esta_registrado("google.com")) 
    
    # Prueba 2: Comprobando un dominio completamente inventado y falso
    print("¿El dominio 'un-dominio-falso-que-no-existe.com' está registrado?")
    print(esta_registrado("un-dominio-falso-que-no-existe.com"))
