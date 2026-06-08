import dns.resolver # Requiere instalación previa: pip install dnspython

# ==============================================================================
# Descripción del Programa:
# Este script realiza una enumeración DNS (Domain Name System) sobre un 
# dominio objetivo. Su propósito es extraer configuraciones clave comprobando 
# varios tipos de registros (A, MX, NS, TXT, etc.). Esto es vital en la fase 
# de recolección de información (Information Gathering) para identificar 
# servidores de correo, direcciones IP, servidores de nombres y verificar 
# políticas de seguridad (como los registros SPF).
# ==============================================================================

# Definimos el dominio que queremos investigar
dominio_objetivo = "scanme.nmap.org" 

# Lista de los tipos de registros DNS más comunes que vamos a consultar
# A y AAAA: Direcciones IPv4 e IPv6
# CNAME: Nombres canónicos (alias)
# MX: Servidores de intercambio de correo
# NS: Servidores de nombres (Name Servers)
# SOA: Inicio de autoridad (Start of Authority)
# TXT: Registros de texto (a menudo contienen reglas de seguridad o verificaciones)
tipos_registros = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

# Creamos un objeto resolutor DNS
resolutor_dns = dns.resolver.Resolver()

# Iteramos sobre cada tipo de registro en nuestra lista
for tipo_registro in tipos_registros:
    
    # Intentamos realizar la consulta DNS para el dominio y el tipo de registro actual
    try:
        respuestas = resolutor_dns.resolve(dominio_objetivo, tipo_registro)
    except dns.resolver.NoAnswer:
        # Si el servidor no tiene una respuesta para este tipo de registro en particular,
        # simplemente lo ignoramos y continuamos con el siguiente en el bucle.
        continue
    except Exception as e:
        # Capturamos cualquier otro error por seguridad
        print(f"[!] Error al consultar el registro {tipo_registro}: {e}")
        continue
    
    # Si encontramos registros exitosamente, los imprimimos en pantalla
    print(f"\n[+] Registros DNS para {dominio_objetivo} (Tipo: {tipo_registro}):")
    for datos_registro in respuestas:
        print(f"    -> {datos_registro}")

#Explicación del Código:

#Librería dnspython: Utilizamos el módulo dns.resolver de esta librería, el cual nos facilita realizar consultas DNS y procesar las respuestas de forma conveniente.

#Tipos de Registros: Consultar distintos registros revela diferentes piezas del rompecabezas. Por ejemplo, los registros A nos dan las direcciones IP detrás del dominio, los registros MX nos revelan qué servicio maneja sus correos (ej. Outlook, Google Workspace), y los registros TXT pueden revelar políticas anti-spam como SPF.

#Objeto Resolver: Utilizamos dns.resolver.Resolver() y su método .resolve(), pasándole como parámetros nuestro dominio y el tipo de registro iterado en ese momento.

#Manejo del Error NoAnswer: Es completamente normal que un dominio no tenga todos los tipos de registros configurados (por ejemplo, podría no tener direcciones IPv6 "AAAA"). Para evitar que el programa colapse, capturamos el error dns.resolver.NoAnswer y usamos continue para pasar al siguiente registro de la lista silenciosamente.
