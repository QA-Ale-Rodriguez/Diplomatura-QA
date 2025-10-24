import requests

BASE_URL = "https://pokeapi.co/api/v2"


# CASO 1: berry/1 (Pomeg Berry)

def test_caso_1_berry_pomeg():
    print("\n--- Ejecutando Caso 1: berry/1 ---")
    response = requests.get(f"{BASE_URL}/berry/1/")
    
    # 1. Verificar que la solicitud fue exitosa (código 200)
    assert response.status_code == 200, f"Error en la solicitud: Código {response.status_code}"
    
    data = response.json()
    
    # 2. Verificar que el size sea 20
    assert data["size"] == 20, f"Fallo en size. Esperado: 20, Obtenido: {data['size']}"
    print(f"✅ Size verificado: {data['size']}")
    
    # 3. Verificar que el soil_dryness sea 15
    assert data["soil_dryness"] == 15, f"Fallo en soil_dryness. Esperado: 15, Obtenido: {data['soil_dryness']}"
    print(f"✅ Soil_dryness verificado: {data['soil_dryness']}")
    
    # 4. Verificar que en firmness, el name sea soft
    assert data["firmness"]["name"] == "soft", f"Fallo en firmness. Esperado: 'soft', Obtenido: {data['firmness']['name']}"
    print(f"✅ Firmness verificado: {data['firmness']['name']}")

    return data["size"], data["soil_dryness"] # Retornamos estos valores para usarlos en el Caso 2


# CASO 2: berry/2 (Cheri Berry)

def test_caso_2_berry_cheri(size_anterior, soil_dryness_anterior):
    print("\n--- Ejecutando Caso 2: berry/2 ---")
    response = requests.get(f"{BASE_URL}/berry/2/")
    
    assert response.status_code == 200, f"Error en la solicitud: Código {response.status_code}"
    
    data = response.json()
    
    # 1. Verificar que en firmness, el name sea super-hard
    assert data["firmness"]["name"] == "super-hard", f"Fallo en firmness. Esperado: 'super-hard', Obtenido: {data['firmness']['name']}"
    print(f"✅ Firmness verificado: {data['firmness']['name']}")
    
    # 2. Verificar que el size sea mayor al del punto anterior (size_anterior = 20)
    assert data["size"] > size_anterior, f"Fallo en size. Esperado: > {size_anterior}, Obtenido: {data['size']}"
    print(f"✅ Size verificado: {data['size']} (Mayor que {size_anterior})")
    
    # 3. Verificar que el soil_dryness sea igual al del punto anterior (soil_dryness_anterior = 15)
    assert data["soil_dryness"] == soil_dryness_anterior, f"Fallo en soil_dryness. Esperado: {soil_dryness_anterior}, Obtenido: {data['soil_dryness']}"
    print(f"✅ Soil_dryness verificado: {data['soil_dryness']} (Igual a {soil_dryness_anterior})")


# CASO 3: pokemon/pikachu

def test_caso_3_pikachu():
    print("\n--- Ejecutando Caso 3: pokemon/pikachu ---")
    response = requests.get(f"{BASE_URL}/pokemon/pikachu/")
    
    assert response.status_code == 200, f"Error en la solicitud: Código {response.status_code}"
    
    data = response.json()
    base_experience = data["base_experience"]
    
    # 1. Verificar que su experiencia base es mayor a 10 y menor a 1000
    assert 10 < base_experience < 1000, f"Fallo en base_experience. Esperado: 10 < X < 1000, Obtenido: {base_experience}"
    print(f"✅ Base_experience verificado: {base_experience} (Está entre 10 y 1000)")
    
    # 2. Verificar que su tipo es "electric"
    # El tipo se encuentra en un array de objetos: data["types"][i]["type"]["name"]
    tipos = [t["type"]["name"] for t in data["types"]]
    
    assert "electric" in tipos, f"Fallo en tipo. Esperado: 'electric' esté en, Obtenido: {tipos}"
    print(f"✅ Tipo verificado: {'electric' in tipos} (Tipos encontrados: {', '.join(tipos)})")


# EJECUCIÓN DE PRUEBAS

if __name__ == "__main__":
    try:
        # Ejecutar Caso 1 y obtener los valores necesarios
        size_c1, dryness_c1 = test_caso_1_berry_pomeg()
        
        # Ejecutar Caso 2 usando los valores del Caso 1
        test_caso_2_berry_cheri(size_c1, dryness_c1)
        
        # Ejecutar Caso 3
        test_caso_3_pikachu()
        
        print("\n==================================")
        print("Estatus 200 ok, todas las pruebas pasaron exitosamente")
        print("==================================")
        
    except AssertionError as e:
        print("\n==================================")
        print(f" Error, una o varias pruebas fallaron \n{e}")
        print("==================================")
    except requests.exceptions.RequestException as e:
        print("\n==================================")
        print(f" ERROR 500 CONEXIÓN CON LA API: {e}")
        print("==================================")