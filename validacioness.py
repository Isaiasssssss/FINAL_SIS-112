#Niños 1-12:
        if (edad >= 1 and edad <= 12) and (genero == "HOMBRE" or genero == "MUJER"):
            if hemoglobina < 11.5:
                estadohemoglobina = "DEFICIENTE"
            elif hemoglobina >= 11.5 and hemoglobina <= 14.5:
                estadohemoglobina = "NORMAL"
            else:
                estadohemoglobina = "EXCESO"
        
            if globulosblancos < 5000:
                estadoglobulosblancos = "DEFICIENTE"
            elif globulosblancos >= 5000 and globulosblancos <= 13000:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
            
            if globulosrojos < 4100000:
                estadoglobulosrojos = "DEFICIENTE"
            elif globulosrojos >= 4100000 and globulosrojos <= 550000:
                estadoglobulosrojos = "NORMAL"
            else:
                estadoglobulosrojos = "EXCESO"
    
            if plaquetas < 150000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 150000 and plaquetas <= 450000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 100:
                estadoglucosa = "NORMAL"
            else:
                estadoglucosa = "EXCESO"
        
            if creatinina < 0.3:
                estadocreatinina = "DEFICIENTE"
            elif creatinina >= 0.3 and creatinina <= 0.7:
                estadocreatinina = "NORMAL"
            else:
                estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.2:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.2 and bilirrubina <= 1.0:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 170:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
            if sodio < 135:
                estadosodio = "DEFICIENTE"
            elif sodio >= 135 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.5:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 9.0:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 9.0 and calcio <= 11.0:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
    

        # Adolescentes 13-18:
        if (edad >= 13 and edad <= 18) and (genero == "HOMBRE" or genero == "MUJER"):
            if genero == "HOMBRE":
                if globulosrojos < 4500000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4500000 and globulosrojos <= 590000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
            elif genero == "MUJER":
                if globulosrojos < 4100000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4100000 and globulosrojos <= 550000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
            
            if hemoglobina < 12.0:
                estadohemoglobina = "DEFICIENTE"
            elif hemoglobina >= 12.0 and hemoglobina <= 16.0:
                estadohemoglobina = "NORMAL"
            else:
                estadohemoglobina = "EXCESO"
                
            if globulosblancos < 4500:
                estadoglobulosblancos = "DEFICIENTE"
            elif globulosblancos >= 4500 and globulosblancos <= 11000:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
    
            if plaquetas < 150000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 150000 and plaquetas <= 450000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 100:
                estadoglucosa = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if creatinina < 0.5:
                estadocreatinina = "DEFICIENTE"
            elif creatinina >= 0.5 and creatinina <= 1.0:
                estadocreatinina = "NORMAL"
            else:
                estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.1:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.1 and bilirrubina <= 1.2:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 170:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
        
            if sodio < 135:
                estadosodio = "DEFICIENTE"
            elif sodio >= 135 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.0:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 9.0:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 9.0 and calcio <= 10.5:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
    
        # Adultos 18-65:
        if (edad >= 18 and edad <= 65) and (genero == "HOMBRE" or genero == "MUJER"):
            if genero == "HOMBRE":
                if hemoglobina < 13.8:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 13.8 and hemoglobina <= 17.2:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                    
                if globulosrojos < 4700000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4700000 and globulosrojos <= 610000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
                    
            elif genero == "MUJER":
                if hemoglobina < 12.1:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 12.1 and hemoglobina <= 15.1:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                    
                if globulosrojos < 4200000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4200000 and globulosrojos <= 540000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
        
            if globulosblancos < 4500:
                estadoglobulosblancos = "DEFICIENTE"
            elif globulosblancos >= 4500 and globulosblancos <= 11000:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
    
            if plaquetas < 150000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 150000 and plaquetas <= 400000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 100:
                estadoglucosa = "NORMAL"
            else:
                estadoglucosa = "EXCESO"
        
            if genero == "HOMBRE":
                if creatinina < 0.7:
                    estadocreatinina = "DEFICIENTE"
                elif creatinina >= 0.7 and creatinina <= 1.3:
                    estadocreatinina = "NORMAL"
                else:
                    estadocreatinina = "EXCESO"
        
            elif genero == "MUJER":
                if creatinina < 0.5:
                    estadocreatinina = "DEFICIENTE"
                elif creatinina >= 0.5 and creatinina <= 1.1:
                    estadocreatinina = "NORMAL"
                else:
                    estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.1:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.1 and bilirrubina <= 1.2:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 200:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
        
            if sodio < 135:
                estadosodio = "DEFICIENTE"
            elif sodio >= 135 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.0:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 8.5:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 8.5 and calcio <= 10.5:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
        
        
        # Adultos Mayores > 65:
        if (edad > 65) and (genero == "HOMBRE" or genero == "MUJER"):
            if genero == "HOMBRE":
                if hemoglobina < 12.6:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 12.6 and hemoglobina <= 15.0:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                
                if globulosrojos < 4000000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4000000 and globulosrojos <= 560000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
                    
            elif genero == "MUJER":
                if hemoglobina < 11.5:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 11.5 and hemoglobina <= 14.5:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                    
                if globulosrojos < 3800000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 3800000 and globulosrojos <= 520000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
        
            if globulosblancos < 3800:
                estadoglobulosblancos = "DEFICIENTE"  
            elif globulosblancos >= 3800 and globulosblancos <= 10500:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
    
            if plaquetas < 140000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 140000 and plaquetas <= 400000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 126:
                estadoglucosa = "NORMAL"
            else:
                estadoglucosa = "EXCESO"
        
            if creatinina < 0.6:
                estadocreatinina = "DEFICIENTE"
            elif creatinina >= 0.6 and creatinina <= 1.2:
                estadocreatinina = "NORMAL"
            else:
                estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.1:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.1 and bilirrubina <= 1.2:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 200:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
        
            if sodio < 132:
                estadosodio = "DEFICIENTE"
            elif sodio >= 132 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.0:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 8.5:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 8.5 and calcio <= 10.2:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
       