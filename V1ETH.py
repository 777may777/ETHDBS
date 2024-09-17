import requests
import time
from concurrent.futures import ThreadPoolExecutor

# Configuración
NODOS_RPC = [
    'https://eth.llamarpc.com',    # Nodo RPC 1
    'https://eth-pokt.nodies.app', # Nodo RPC 2
    'https://rpc.ankr.com/eth'     # Nodo RPC 3
]

ARCHIVO_RESULTADO = 'result.txt'  # Nombre del archivo donde se guardarán las direcciones
INTERVALO_VERIFICACION = 15       # Tiempo en segundos entre cada verificación de nuevos bloques
MIN_ETH_VALUE = 0.01              # Valor mínimo de ETH para filtrar transacciones

# Nota de descargo: Este script ha sido creado solo con fines educativos.
# No se asume ninguna responsabilidad por el uso indebido del mismo.

def obtener_numero_bloque_actual(rpc_url):
    """
    Obtiene el número del último bloque de la cadena de bloques de Ethereum.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    try:
        response = requests.post(rpc_url, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        return int(result['result'], 16)
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error al obtener el número de bloque actual desde {rpc_url}: {e}")
        return None

def obtener_transacciones_del_bloque(rpc_url, block_number):
    """
    Obtiene todas las transacciones de un bloque específico.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [hex(block_number), True],
        "id": 1
    }
    try:
        response = requests.post(rpc_url, json=payload, timeout=10)
        response.raise_for_status()
        block = response.json().get('result', {})
        return block.get('transactions', [])
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error al obtener transacciones del bloque {block_number} desde {rpc_url}: {e}")
        return []

def filtrar_direcciones_por_valor(transacciones, min_value):
    """
    Filtra las transacciones que tienen un valor mayor que 'min_value' y devuelve las direcciones.
    """
    direcciones = set()
    for tx in transacciones:
        try:
            # Convertir el valor de la transacción de Wei a ETH
            eth_value = int(tx['value'], 16) / 10**18
            if eth_value > min_value:
                if tx['from']:
                    direcciones.add(tx['from'])
                if tx['to']:
                    direcciones.add(tx['to'])
        except (KeyError, ValueError):
            continue
    return direcciones

def guardar_direcciones_en_archivo(direcciones, archivo):
    """
    Guarda las direcciones en un archivo de texto.
    """
    try:
        with open(archivo, 'a') as f:
            for direccion in direcciones:
                f.write(direccion + '\n')
    except IOError as e:
        print(f"Error al guardar direcciones en el archivo {archivo}: {e}")

def cambiar_rpc(nodo_actual):
    """
    Cambia al siguiente nodo RPC en la lista.
    """
    nuevo_nodo = (nodo_actual + 1) % len(NODOS_RPC)
    print(f"Cambiando al siguiente nodo RPC: {NODOS_RPC[nuevo_nodo]}")
    return nuevo_nodo

def procesar_bloque(rpc_url, numero_bloque_actual):
    """
    Procesa un bloque, obtiene sus transacciones y guarda las direcciones con transacciones mayores al mínimo definido.
    """
    nuevo_numero_bloque = obtener_numero_bloque_actual(rpc_url)
    if nuevo_numero_bloque and nuevo_numero_bloque > numero_bloque_actual:
        print(f"Nuevo bloque detectado: {nuevo_numero_bloque}")
        transacciones = obtener_transacciones_del_bloque(rpc_url, nuevo_numero_bloque)
        direcciones = filtrar_direcciones_por_valor(transacciones, MIN_ETH_VALUE)
        if direcciones:
            guardar_direcciones_en_archivo(direcciones, ARCHIVO_RESULTADO)
            print(f"Direcciones con más de {MIN_ETH_VALUE} ETH del bloque {nuevo_numero_bloque} guardadas en {ARCHIVO_RESULTADO}")
        return nuevo_numero_bloque
    return numero_bloque_actual

def main():
    numero_bloque_actual = None
    nodo_actual = 0  # Empezar con el primer nodo de la lista

    # Intentar obtener el número del bloque inicial utilizando el primer nodo disponible
    while numero_bloque_actual is None:
        rpc_url = NODOS_RPC[nodo_actual]
        numero_bloque_actual = obtener_numero_bloque_actual(rpc_url)
        if numero_bloque_actual is None:
            nodo_actual = cambiar_rpc(nodo_actual)

    print(f"Monitoreando bloques nuevos a partir del bloque: {numero_bloque_actual}")

    with ThreadPoolExecutor(max_workers=2) as executor:
        while True:
            try:
                rpc_url = NODOS_RPC[nodo_actual]
                numero_bloque_actual = procesar_bloque(rpc_url, numero_bloque_actual)
                time.sleep(INTERVALO_VERIFICACION)
            except Exception as e:
                print(f"Error durante el procesamiento: {e}")
                nodo_actual = cambiar_rpc(nodo_actual)  # Cambiar al siguiente nodo RPC en caso de error

if __name__ == '__main__':
    print("Este script fue hecho por 777may777 para fines educativos.")
    main()
