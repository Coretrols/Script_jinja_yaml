import yaml
from jinja2 import Template, TemplateSyntaxError, exceptions

def crea_configuracion_con_yaml():
    try:
        with open('ejemplo.yml','r') as contenedor:
            diccionario = yaml.safe_load(contenedor)    
            # print(type(diccionario))     
            return diccionario
    except OSError as captura_error:
        print( "El error es:", str(captura_error))
        return {"Error": str(captura_error)}
    except yaml.YAMLError as captura_error:
        print( "El error es:", str(captura_error))
        return {"Error": str(captura_error)}
    except Exception as excepcion_generica:
        print(f"Otra excepcion random {excepcion_generica}" )
    # finally:
    #     return 0

def configura_jinja_en_base_yaml(plantilla,diccionario):

    try:
        with open(plantilla,"r") as pjinja:
            lee_Jinja = Template(pjinja.read())
            # print(type(lee_Jinja))
            # print(leerJinja) 
            renderizarJinja =  lee_Jinja.render(diccionario)
            # print(type(renderizarJinja))

           
        nombre = diccionario['diccionario']['elemento1']+ '.txt'

        with open(f'{nombre}','w') as f: 
                f.write(renderizarJinja) 
    except FileNotFoundError as error_encontrar:
        print(f"No se encontro: {error_encontrar}")
    except exceptions.UndefinedError as captura_error:
        print(f"Error al cargar {captura_error}")
    except TypeError as tipo_error:
        print(f"Error de tipo: {tipo_error}")
    except Exception as excepcion_generica:
        print(f"Otra excepcion random {excepcion_generica}")


def main():

    diccionario = crea_configuracion_con_yaml()
    # print(type(diccionario))
    configura_jinja_en_base_yaml('validaconyaml.j2',diccionario)
    # print(type(archivo))

if __name__ == '__main__':
    main()

