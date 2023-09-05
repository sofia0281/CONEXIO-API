import pandas as pd 
from sodapy import Socrata
from statistics import median
from tabulate import tabulate


def api_conection():
    client = Socrata("www.datos.gov.co", None)
    return client

def client_consult(departamento_consulta, municipio_consulta, cultivo_consulta, limite_consulta):
    client = api_conection()
    consult_result = client.get("ch4u-f3i5", limit = limite_consulta,
                                departamento = departamento_consulta,
                                municipio = municipio_consulta, cultivo = cultivo_consulta)
    consult_dataframe = pd.DataFrame.from_records(consult_result)
    return consult_dataframe

def consult_filter(consult_dataframe):
    consult_result = consult_dataframe[["departamento","municipio", "cultivo", 
                                        "topografia", "ph_agua_suelo_2_5_1_0",
                                        "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg"]]
    return consult_result

def consult_data_median(consult_dataframe, dato_a_medir):
    median_result = consult_dataframe[dato_a_medir]
    median_result = median(median_result)
    return median_result

def modify_invalid_data(consult_dataframe, modify_key):
    consult_dataframe[modify_key] = pd.to_numeric(consult_dataframe[modify_key], errors = "coerce")
    consult_dataframe = consult_dataframe.sort_values(by = modify_key, na_position = "first")
    return consult_dataframe


