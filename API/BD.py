import oracledb

class ConexionBD:

    user = "AdminTienda"
    password = "AdminTienda"
    tipoUsuario = "002"


    def validarLogin(correo,contrasena):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "select correo, contrasena from usuario"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        for r in result:
            if r[0] == correo and r[1] == contrasena:
                return True
        return False
    
    def maximoUsuario():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT MAX(idUsuario)+1 FROM usuario"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def agregarUsuario(nombreUsuario, contrasena, correo, nombres, apellidos, telefono):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        print(ConexionBD.maximoUsuario())
        query = "INSERT INTO usuario values('"+str(ConexionBD.maximoUsuario())+"','"+ConexionBD.tipoUsuario+"','"+nombreUsuario+"','"+contrasena+"','"+nombres+"','"+apellidos+"','"+correo+"','"+telefono+"')"
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result

    def consultarEstudiantes():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select u.nombreusuario, u.nombres, u.apellidos, u.contrasena, u.correo, u.telefono from usuario")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def consultarTallas():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select idtalla from talla")
        result = cursor.fetchall()
        connection.close()
        return result

    def consultarUnidades():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select f.nomunidad, p.nomunidad, p.codunidad from unidad f, unidad p where f.codunidad = p.uni_codunidad and f.tipounidad like 'AC'")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def consultarCalendario(periodo:str,mes:str):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "select o.titulo, t.desctipocalendario, c.idestado, c.fechainicio, c.fechafin, o.idobra, c.conseccalendario,t.idtipocalen from obra o,tipocalendario t, calendario c where t.idtipocalen = c.idtipocalen and o.idobra = c.idobra and o.idperiodo = "+periodo+" and extract(MONTH from c.fechainicio) = "+mes+" ORDER BY c.fechainicio"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    def inactivarEventoPeriodo(tipoCalen:str,periodo:str):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "update calendario c set c.idestado = 'Inactivo' where idObra in (select o.idObra from obra o where o.idperiodo = "+periodo+") and c.idtipocalen = '"+tipoCalen+"'"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def consultarEstudianteConvocatoria():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select e.codEstudiante, e.nombre ||' '|| e.apellido, con.idinstrumento, con.idobra ,f.nomUnidad, c.nomUnidad, i.nomInstrumento, cal.conseccalendario + 1 " +
                        "from estudiante e, unidad f, unidad c, convocatoriaEstudiante con, instrumento i, calendario cal " +
                        "where c.codunidad = e.codunidad and f.codunidad = c.uni_codunidad and " +
                        "i.idInstrumento = con.idInstrumento and e.codEstudiante = con.codEstudiante and " +
                        "cal.conseccalendario like " +
                        "(select distinct max(cal.conseccalendario) from calendario cal, convocatoriaestudiante cov " +
                        "where TO_DATE(cal.fechainicio, 'dd/mm/yyyy') like TO_DATE(cov.fechainicio, 'dd/mm/yyyy')) " +
                        "and cal.idobra like con.idobra " +
                        "order by con.calificacion desc")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def consultarLiquidacion(periodo:str):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
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
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "select e.nombre || ' ' || e.apellido, e.codestudiante from participacionestudiante p,estudiante e, obra o where e.codestudiante = p.codestudiante and p.idtipocalen = 'SL' and o.idobra = p.idobra and o.idperiodo = "+periodo
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    def periodoInactivo():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select distinct max(o.idperiodo) from  obra o, calendario c " +
                        "where c.idobra = o.idobra and " + 
                        "(o.idperiodo, c.conseccalendario) in (select o.idperiodo , max(c.conseccalendario) from obra o, calendario c " + 
                        "where c.idobra = o.idobra and lower(c.idtipocalen) like 'en' group by o.idperiodo) " +
                        "and lower(c.idestado) like 'inactivo'")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def obtenerInstrumentos():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select r26.idInstrumento, r26.num from relationship_26 r26 where r26.idobra like " +
                        "(select distinct cal.idobra from calendario cal, convocatoriaestudiante cov " +
                        "where TO_DATE(cal.fechainicio, 'dd/mm/yyyy') like TO_DATE(cov.fechainicio, 'dd/mm/yyyy') and cal.conseccalendario like " +
                        "(select distinct max(cal.conseccalendario) from calendario cal, convocatoriaestudiante cov " + 
                        "where TO_DATE(cal.fechainicio, 'dd/mm/yyyy') like TO_DATE(cov.fechainicio, 'dd/mm/yyyy')))")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def maxIdParticipacion():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select max(consecasis) + 1 from participacionestudiante")
        result = cursor.fetchall()
        connection.close()
        return result

    def agregarParticipacion(consecasis:str, idobra:str, conseccalendario:str, codestudiante:str):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "INSERT INTO participacionestudiante values("+consecasis+",'"+idobra+"','"+ "SL" +"',"+conseccalendario+",'" + codestudiante + "')"
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result
    
    def inactivarConvocatoria(conseccalendario:str):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "update calendario set idestado = 'Inactivo' where conseccalendario like " + conseccalendario
        cursor.execute(query)
        connection.commit()
        connection.close()

    def obtenerCalendario(periodo):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "select o.titulo, t.desctipocalendario, c.idestado, c.fechainicio, c.fechafin, o.idobra, c.conseccalendario,t.idtipocalen from obra o,tipocalendario t, calendario c where t.idtipocalen = c.idtipocalen and o.idobra = c.idobra and o.idperiodo = "+periodo+" ORDER BY c.fechainicio"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result
    
    def subirAsistencia(estudiante,event):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "select max(consecasis) from participacionestudiante"
        cursor.execute(query)
        max = cursor.fetchone()[0]
        print(estudiante)
        print(event)
        query = "insert into participacionestudiante select "+str(max+1)+",c.idobra,c.idtipocalen,c.conseccalendario,"+estudiante+" from calendario c where c.conseccalendario = "+str(event)
        print(query)
        cursor.execute(query)
        connection.commit()
        connection.close()
        return None
    
    def obtenerPeriodos():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port=1521, service_name="xe")
        cursor = connection.cursor()
        query = "select idperiodo from periodo"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    
    