import requests

def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return None

def mostrar_informacion_clima(datos):
    if datos:
        ciudad = datos['name']
        temperatura = datos['main']['temp']
        descripcion = datos['weather'][0]['description']
        humedad = datos['main']['humidity']
        velocidad_viento = datos['wind']['speed']

        print(f"Ciudad: {ciudad}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Descripción: {descripcion}")
        print(f"Humedad: {humedad}%")
        print(f"Velocidad del viento: {velocidad_viento} m/s")
    else:
        print("No se pudo obtener la información del clima.")

if __name__ == "__main__":
    ciudad = input("Ingrese el nombre de la ciudad: ")
    api_key = "3e164c0f9dfffdd1fca239aa96c16b56"  # Reemplaza esto con tu clave de API de OpenWeatherMap
    datos_clima = obtener_clima(ciudad, api_key)
    mostrar_informacion_clima(datos_clima)