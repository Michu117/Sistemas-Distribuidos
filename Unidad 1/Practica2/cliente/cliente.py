from pathlib import Path
from time import sleep

BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ENTRADA = BASE_DIR / "" / "entrada_servidor.txt"
ARCHIVO_SALIDA = BASE_DIR / "" / "salida_servidor.txt"
LATENCIA_SIMULADA = 3
INTERVALO_ESPERA = 3


# envia un mensaje y espera la respuesta del servidor.
def enviar_mensaje(mensaje: str) -> str:
    ARCHIVO_ENTRADA.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVO_SALIDA.write_text("", encoding="utf-8")
    ARCHIVO_ENTRADA.write_text(mensaje, encoding="utf-8")
    sleep(LATENCIA_SIMULADA)

    while True:
        respuesta = ARCHIVO_SALIDA.read_text(encoding="utf-8")
        if respuesta:
            return respuesta
        sleep(INTERVALO_ESPERA)

# enviar mensajes consecutivos al servidor
def ejecutar_cliente() -> None:
    while True:
        try:
            mensaje = input("Mensaje: ")
        except (EOFError, KeyboardInterrupt):
            print("\nCliente detenido.")
            break

        if not mensaje:
            print("El mensaje no puede estar vacío.")
            continue

        respuesta = enviar_mensaje(mensaje)
        print(f"Respuesta: {respuesta}")


if __name__ == "__main__":
    ejecutar_cliente()
