import oracledb
import random

class ConexionBD:

    user = "AdminTienda"
    password = "AdminTienda"
    tipoUsuario = "002"
    port = 1521
    categoriaCatalogo = 1
    seleccionTipoCamiseta = str
    idUsuarioValido: str
    seleccionCatalogo = str
    codigoFactura = str
    total = str
    
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
                ConexionBD.codigoFactura = ConexionBD.maximaFactura()
                ConexionBD.nuevaFactura()
                return True
        return False
    
    def maximaFactura():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT COUNT(codigoFactura)+1 FROM factura"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def nuevaFactura():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "INSERT INTO factura values('"+str(ConexionBD.codigoFactura)+"','"+str(ConexionBD.idUsuarioValido)+"')"
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result
        
    def maximoDetalleFactura():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT COUNT(iddetallefactura)+1 FROM detallefactura"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def maximoDatoFactura():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT COUNT(iddatosfactura)+1 FROM datosfactura"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def maximoUsuario():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT COUNT(idUsuario)+1 FROM usuario"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def maximaEstampa():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "SELECT COUNT(idestampa)+1 FROM estampa"
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    
    def agregarUsuario(nombreUsuario, contrasena, correo, nombres, apellidos, telefono):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        print(ConexionBD.maximoUsuario())
        credito = random.randint(80000,30000000)
        query = "INSERT INTO usuario values('"+str(ConexionBD.maximoUsuario())+"','"+ConexionBD.tipoUsuario+"','"+nombreUsuario+"','"+contrasena+"','"+nombres+"','"+apellidos+"','"+correo+"','"+telefono+"','"+str(credito)+"')"
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
    
    def seleccionTipo(seleccionTipoCamiseta):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        seleccionTipoCamiseta = seleccionTipoCamiseta[-6:]
        ConexionBD.seleccionTipoCamiseta = seleccionTipoCamiseta
        print(seleccionTipoCamiseta)
        return seleccionTipoCamiseta
    
    def estampaSeleccionada(seleccion):
        ConexionBD.seleccionCatalogo = seleccion
        print(seleccion)
        return seleccion
    
    def consultarStock():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select idmodelocamiseta, stock from modelocamiseta where idmodelocamiseta like '"+str(ConexionBD.seleccionTipoCamiseta)+"'")
        result = cursor.fetchall()
        connection.close()
        print(result)
        return result
    
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
            cursor.execute("select e.idestampa, e.nombre, t.nombre, e.imagen1, e.calificacion, e.precio, u.nombreusuario from estampa e, tematica t, usuario u where e.idtematica = t.idtematica and e.idusuario = u.idusuario order by e.idusuario DESC")
            result = cursor.fetchall()
            connection.close()
        else:
            cursor.execute("select e.idestampa, e.nombre, t.nombre, e.imagen1, e.calificacion, e.precio, u.nombreusuario from estampa e, tematica t, usuario u where e.idtematica = t.idtematica and e.idusuario = u.idusuario order by t.idtematica DESC")
            result = cursor.fetchall()
            connection.close()
        #print(result)
        return result
    
    def consultarEstampaSeleccionada():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        seleccion = ConexionBD.seleccionCatalogo
        cursor.execute("select e.idestampa, e.nombre, e.descripcion, t.nombre, e.imagen1, e.imagen2, e.imagen3, e.calificacion, e.precio, u.nombreusuario from estampa e, tematica t, usuario u where e.idtematica = t.idtematica and e.idusuario = u.idusuario and e.idestampa ="+seleccion+"")
        result = cursor.fetchall()
        connection.close()
        return result

    def consultarModeloCamiseta():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        cursor.execute("select c.idmodelocamiseta, c.modelo, c.stock, m.nombrematerial from modelocamiseta c, material m where m.idmaterial = c.idmaterial")
        result = cursor.fetchall()
        print(result)
        connection.close()
        return result
    
    def precioEstampa():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        seleccion_estampa = ConexionBD.seleccionCatalogo
        query = "SELECT precio FROM estampa WHERE idestampa ="+str(seleccion_estampa)+""
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result[0][0]
    
    def agregarCarrito(idmodelocamiseta,idtalla,cantidad,colorcamiseta):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        print(ConexionBD.maximaEstampa())
        subtotal = (ConexionBD.precioEstampa() * cantidad)
        print(subtotal)
        query = "INSERT INTO detallefactura values('"+str(ConexionBD.maximoDetalleFactura())+"','"+str(ConexionBD.codigoFactura)+"','"+idmodelocamiseta+"','"+idtalla+"','"+str(ConexionBD.seleccionCatalogo)+"','"+str(cantidad)+"','"+colorcamiseta+"','"+str(subtotal)+"')"
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result
    
    def consultarCarrito():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        seleccion = ConexionBD.seleccionCatalogo
        cursor.execute("select e.imagen1, e.nombre, t.modelo, m.nombrematerial, d.idtalla, d.cantidad, d.colorcamiseta, d.subtotal, d.iddetallefactura from estampa e, modelocamiseta t, material m, detallefactura d where e.idestampa = d.idestampa and t.idmodelocamiseta = d.idmodelocamiseta and m.idmaterial = t.idmaterial and d.codigofactura ="+str(ConexionBD.codigoFactura)+"")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def totalCarrito():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        seleccion = ConexionBD.seleccionCatalogo
        cursor.execute("select SUM(subtotal) from detallefactura where codigofactura ="+str(ConexionBD.codigoFactura)+"")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def totalCarritointerno():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        seleccion = ConexionBD.seleccionCatalogo
        cursor.execute("select SUM(subtotal) from detallefactura where codigofactura ="+str(ConexionBD.codigoFactura)+"")
        result = cursor.fetchall()
        connection.close()
        return result[0][0]
    
    def eliminarProducto(datoEliminacion):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "DELETE FROM detallefactura WHERE iddetallefactura ="+str(datoEliminacion)+""
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result
    
    def consultarCredito():
        oracledb.init_oracle_client()
        connection = oracledb.connect(user= ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        seleccion = ConexionBD.seleccionCatalogo
        cursor.execute("select credito from usuario where idusuario ="+str(ConexionBD.idUsuarioValido)+"")
        result = cursor.fetchall()
        connection.close()
        return result
    
    def agregarDatosFactura(numDocumento,direccionEntrega):
        oracledb.init_oracle_client()
        connection = oracledb.connect(user=ConexionBD.user, password=ConexionBD.password,host="localhost", port = ConexionBD.port, service_name="xe")
        cursor = connection.cursor()
        query = "INSERT INTO datosfactura values('"+str(ConexionBD.maximoDatoFactura())+"','"+str(ConexionBD.codigoFactura)+"','"+str(ConexionBD.totalCarritointerno())+"','"+numDocumento+"','"+direccionEntrega+"','En proceso')"
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result