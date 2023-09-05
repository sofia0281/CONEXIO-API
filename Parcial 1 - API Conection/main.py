from UI import UI
from API import API

mensaje_parada = "SI"

while(mensaje_parada == "SI"):
    
    recibir_parametros = UI.Ingreso_usuario()
    departamento = recibir_parametros.departamento()
    municipio = recibir_parametros.municipio()
    cultivo = recibir_parametros.cultivo()
    limite = recibir_parametros.limite()

    try:
        resultado = API.client_consult(departamento, municipio, cultivo, limite)
        resultado = API.consult_filter(resultado)
        imprimir_tabla = UI.Imprimir_datos()
        imprimir_tabla.tabulador_registros(resultado)
        mediana_result = []
        resultado = API.modify_invalid_data(resultado, "ph_agua_suelo_2_5_1_0")
        resultado = API.modify_invalid_data(resultado, "f_sforo_p_bray_ii_mg_kg")
        resultado = API.modify_invalid_data(resultado, "potasio_k_intercambiable_cmol_kg")
        mediana_result.append(str(API.consult_data_median(resultado, "ph_agua_suelo_2_5_1_0")))
        mediana_result.append(str(API.consult_data_median(resultado, "f_sforo_p_bray_ii_mg_kg")))
        mediana_result.append(str(API.consult_data_median(resultado, "potasio_k_intercambiable_cmol_kg")))
        imprimir_medianas = UI.Imprimir_datos()
        imprimir_medianas.imprimir_medianas([mediana_result])
    except:
        print("Datos erroneos... Por favor, revise los datos ingresados")
    
    mensaje_parada = str(input("Desea realizar más consultas?\nDigite (SI o NO): ")).strip().upper()

