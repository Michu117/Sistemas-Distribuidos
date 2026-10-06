from pathlib import Path
from time import sleep

BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ENTRADA = BASE_DIR / "" / "entrada_servidor.txt"
ARCHIVO_SALIDA = BASE_DIR / "" / "salida_servidor.txt"
INTERVALO_REVISION = 3

#  upper para convertir el mensaje recibido a mayúsculas
def procesar_mensaje(mensaje: str) -> str:
    return mensaje.upper()

# revisa la entrada continuamente y escribe los mensajes nuevos
def ejecutar_servidor() -> None:
    ARCHIVO_ENTRADA.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVO_ENTRADA.touch(exist_ok=True)
    ARCHIVO_SALIDA.touch(exist_ok=True)

    ultima_version: tuple[int, str] | None = None
    print("Servidor iniciado")

    try:
        while True:
            try:
                version = ARCHIVO_ENTRADA.stat().st_mtime_ns
                mensaje = ARCHIVO_ENTRADA.read_text(encoding="utf-8")
            except OSError as error:
                print(f"No se pudo leer la entrada: {error}")
                sleep(INTERVALO_REVISION)
                continue

            identificador = (version, mensaje)
            if mensaje and identificador != ultima_version:
                respuesta = procesar_mensaje(mensaje)
                try:
                    ARCHIVO_SALIDA.write_text(respuesta, encoding="utf-8")
                except OSError as error:
                    print(f"No se pudo escribir la salida: {error}")
                else:
                    print(f"Mensaje procesado: {mensaje.rstrip()!r}")
                    ultima_version = identificador
            elif not mensaje:
                # archivo vacío
                ultima_version = identificador

            sleep(INTERVALO_REVISION)
    except KeyboardInterrupt:
        print("\nServidor detenido.")


if __name__ == "__main__":
    ejecutar_servidor()
