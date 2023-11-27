import oracledb
import random

class ConexionBD:

    user = "AdminTienda"
    password = "AdminTienda"
    tipoUsuario = "002"
    port = 1521
    categoriaCatalogo = 1
    idUsuarioValido: str

    def validarLogin(correo,contrasena):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "select idusuario, correo, contrasena from usuario"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        for r in result:
            if r[1] == correo and r[2] == contrasena:
                ConexionBD.idUsuarioValido = r[0]
                return True
        return False
    
    def maximoUsuario():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT MAX(idUsuario)+1 FROM usuario"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def maximaEstampa():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT MAX(idestampa)+1 FROM estampa"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def agregarUsuario(nombreUsuario, contrasena, correo, nombres, apellidos, telefono):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        print(ConexionBD.maximoUsuario())
        query = "INSERT INTO usuario values('"+str(ConexionBD.maximoUsuario())+"','"+ConexionBD.tipoUsuario+"','"+nombreUsuario+"','"+contrasena+"','"+nombres+"','"+apellidos+"','"+correo+"','"+telefono+"')"
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result
    
    def agregarEstampa(nombre,descripcion,imagen1,imagen2,imagen3,precio,idtematica):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        print(ConexionBD.maximaEstampa())
        idUsuario = ConexionBD.idUsuarioValido
        print(idUsuario)
        calificacion = random.randint(0,100)
        estado = "Activo"
        query = "INSERT INTO estampa values('"+str(ConexionBD.maximaEstampa())+"','"+idUsuario+"','"+idtematica+"','"+nombre+"','"+descripcion+"','"+imagen1+"','"+imagen2+"','"+imagen3+"','"+str(calificacion)+"','"+str(precio)+"','"+estado+"')"
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result
    
    def consultarTallas():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select idtalla from talla")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def consultarTematica():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select idtematica, nombre from tematica")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def consultarCategoria(categoria):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        ConexionBD.categoriaCatalogo = categoria
        return categoria
        
    def consultarEstampas():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        categoria = ConexionBD.consultarCategoria(ConexionBD.categoriaCatalogo)
        if categoria == 2:
            cursor.execute("select e.idestampa, e.nombre, t.nombre, e.imagen1, e.calificacion, e.precio, u.nombreusuario from estampa e, tematica t, usuario u where e.idtematica = t.idtematica and e.idusuario = u.idusuario order by e.calificacion DESC")
            result = cursor.fetchall()
            connection.close()
        elif categoria == 1:
            cursor.execute("select e.idestampa, e.nombre, t.nombre, e.imagen1, e.calificacion, e.precio, u.nombreusuario from estampa e, tematica t, usuario u where e.idtematica = t.idtematica and e.idusuario = u.idusuario order by e.idusuario")
            result = cursor.fetchall()
            connection.close()
        else:
            cursor.execute("select e.idestampa, e.nombre, t.nombre, e.imagen1, e.calificacion, e.precio, u.nombreusuario from estampa e, tematica t, usuario u where e.idtematica = t.idtematica and e.idusuario = u.idusuario order by t.idtematica")
            result = cursor.fetchall()
            connection.close()
        #print(result)
        return result
    
    def consultarLiquidacion(periodo:str):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select e.nombre ||' '|| e.apellido Estudiante, e.codestudiante codigo, un.nomunidad facultad, e.correo correo, " +
                        "sum(trunc(mod((c.fechafin - c.fechainicio)*24,24))) Nohoras " +
                        "from estudiante e, unidad u, unidad un, calendario c, participacionestudiante p, obra o " +
                        "where e.codestudiante = p.codestudiante and e.codunidad = u.codunidad and " +
                        "u.uni_codunidad = un.codunidad and c.conseccalendario = p.conseccalendario and " +
                        "o.idobra = c.idobra and o.idperiodo like "+ periodo +" " +
                        "group by e.nombre ||' '|| e.apellido , e.codestudiante , un.nomunidad, e.correo")
        result = cursor.fetchall()
        connection.close()
        return result

    def obtenerSeleccionados(periodo:str):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "select e.nombre || ' ' || e.apellido, e.codestudiante from participacionestudiante p,estudiante e, obra o where e.codestudiante = p.codestudiante and p.idtipocalen = 'SL' and o.idobra = p.idobra and o.idperiodo = "+periodo
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    
    