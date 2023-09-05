from tabulate import tabulate

class Ingreso_usuario:
    
    def departamento (self):
        departamento_ingresado=str(input ("Ingrese el departamento del que desea conocer sus datos:")).upper().strip()
        return departamento_ingresado
    
    def municipio (self):
        municipio_ingresado= str(input ("Ingrese el municipio  del departamento que desea conocer sus datos: ")).upper().strip()
        return municipio_ingresado

    def cultivo (self):
        cultivo_ingresado= str(input ("Ingrese el tipo de cultivo: ")).capitalize().strip()
        return cultivo_ingresado
    
    def limite(self):
        limite_registros=int(input ("Ingrese el número de registros que desea visualizar: "))
        return limite_registros
    


class Imprimir_datos:
    
    def tabulador_registros(self,consulta_DataFrame):
        
        titulo = ["DEPARTAMENTO", "MUNICIPIO", "CULTIVO", "TOPOLOGÍA","PH DEL SUELO", "FOSFORO", "POTASIO"]
        tabla = tabulate(consulta_DataFrame, titulo, tablefmt = 'outline')
        print(tabla)
    
    def imprimir_medianas(self,mediana_result):
        print ("Medianas:")
        titulo =["PH DEL SUELO", "FOSFORO","POTASIO"]
        tabla = tabulate (mediana_result,titulo,tablefmt = 'outline')
        print(tabla)
    