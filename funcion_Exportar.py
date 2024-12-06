def exportar_con_resultados():
    datos = f"""
    -------- Datos Personales --------
    Nombre: {nombre}
    Apellido: {apellido}
    Edad: {edad}
    Género: {genero}

    -------- Resultados del Análisis --------
    Hemoglobina:
        Valor: {hemoglobina}
        Estado: {estadohemoglobina}
    Plaquetas:
        Valor: {plaquetas}
        Estado: {estadoplaquetas}
    Bilirrubina:
        Valor: {bilirrubina}
        Estado: {estadobilirrubina}
    Glóbulos Rojos:
        Valor: {globulosrojos}
        Estado: {estadoglobulosrojos}
    Glóbulos Blancos:
        Valor: {globulosblancos}
        Estado: {estadoglobulosblancos}
    Glucosa:
        Valor: {glucosa}
        Estado: {estadoglucosa}
    Creatinina:
        Valor: {creatinina}
        Estado: {estadocreatinina}
    Colesterol:
        Valor: {colesterol}
        Estado: {estadocolesterol}
    Sodio:
        Valor: {sodio}
        Estado: {estadosodio}
    Potasio:
        Valor: {potasio}
        Estado: {estadopotasio}
    Calcio:
        Valor: {calcio}
        Estado: {estadocalcio}

    -------- Fin del Reporte --------
    """

    # Guardar en un archivo de texto
    with open("resultados_completos.txt", "w") as archivo:
        archivo.write(datos)

    messagebox.showinfo("Guardado", "Datos y resultados exportados a 'resultados_completos.txt'")
