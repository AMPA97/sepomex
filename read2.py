
def read():
    CP=[]
    with open("./archivos/CPcopia.txt", "r") as f:
        next(f, None)
        next(f, None)    
        for line in f :
            lista=line.split("|")
            dic={
                'Codigo_postal':lista[0],
                'nombre_acentamiento':lista[1],
                'tipo_acentamiento':lista[2],
                'municipio':lista[3],
                'estado':lista[4],
                'ciudad':lista[5],
                'd_CP':lista[6],
                'c_estado':lista[7],
                'c_oficina':lista[8],
                'c_CP':lista[9],
                'c_tipo_asenta':lista[10],
                'c_mnpio':lista[11],
                'id_asenta_cpcons':lista[12],
                'tipo_zona':lista[13],
                'c_cve_ciuda':lista[14]
            }
            CP.append(dic)  

    print(CP)
     

def run():
    read()
if __name__=="__main__":
    run() 
    