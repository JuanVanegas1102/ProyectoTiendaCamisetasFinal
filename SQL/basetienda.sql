/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     07/11/2023 02:23:09 a. m.                    */
/*==============================================================*/


alter table DETALLEFACTURA
   drop constraint FK_DETALLEF_COMPONE_TALLA;

alter table DETALLEFACTURA
   drop constraint FK_DETALLEF_CONTIENE_FACTURA;

alter table DETALLEFACTURA
   drop constraint FK_DETALLEF_ESPECIFIC_MODELOCA;

alter table ESTAMPA
   drop constraint FK_ESTAMPA_CREA_USUARIO;

alter table ESTAMPA
   drop constraint FK_ESTAMPA_TIENE_TEMATICA;

alter table FACTURA
   drop constraint FK_FACTURA_GENERA_USUARIO;

alter table TIPOESTAMPA
   drop constraint FK_TIPOESTA_AGREGA_DETALLEF;

alter table TIPOESTAMPA
   drop constraint FK_TIPOESTA_PERTENECE_ESTAMPA;

alter table USUARIO
   drop constraint FK_USUARIO_ES_TIPOUSUA;

drop index ESPECIFICA_FK;

drop index COMPONE_FK;

drop index CONTIENE_FK;

drop table DETALLEFACTURA cascade constraints;

drop index TIENE_FK;

drop index CREA_FK;

drop table ESTAMPA cascade constraints;

drop index GENERA_FK;

drop table FACTURA cascade constraints;

drop table MODELOCAMISETA cascade constraints;

drop table TALLA cascade constraints;

drop table TEMATICA cascade constraints;

drop index PERTENECE_FK;

drop index AGREGA_FK;

drop table TIPOESTAMPA cascade constraints;

drop table TIPOUSUARIO cascade constraints;

drop index ES_FK;

drop table USUARIO cascade constraints;

/*==============================================================*/
/* Table: DETALLEFACTURA                                        */
/*==============================================================*/
create table DETALLEFACTURA 
(
   IDDETALLEFACTURA     VARCHAR2(10)         not null,
   CODIGOFACTURA        VARCHAR2(12)         not null,
   IDMODELOCAMISETA     VARCHAR2(10)         not null,
   IDTALLA              VARCHAR2(3)          not null,
   CANTIDAD             NUMBER(1),
   COLORCAMISETA        VARCHAR2(6)          not null,
   constraint PK_DETALLEFACTURA primary key (IDDETALLEFACTURA)
);

/*==============================================================*/
/* Index: CONTIENE_FK                                           */
/*==============================================================*/
create index CONTIENE_FK on DETALLEFACTURA (
   CODIGOFACTURA ASC
);

/*==============================================================*/
/* Index: COMPONE_FK                                            */
/*==============================================================*/
create index COMPONE_FK on DETALLEFACTURA (
   IDTALLA ASC
);

/*==============================================================*/
/* Index: ESPECIFICA_FK                                         */
/*==============================================================*/
create index ESPECIFICA_FK on DETALLEFACTURA (
   IDMODELOCAMISETA ASC
);

/*==============================================================*/
/* Table: ESTAMPA                                               */
/*==============================================================*/
create table ESTAMPA 
(
   IDESTAMPA            VARCHAR2(6)          not null,
   IDUSUARIO            VARCHAR2(8)          not null,
   IDTEMATICA           VARCHAR2(5)          not null,
   NOMBRE               VARCHAR2(30)         not null,
   DESCRIPCION          VARCHAR2(100)        not null,
   IMAGEN1              CLOB                 not null,
   IMAGEN2              CLOB,
   IMAGEN3              CLOB,
   CALIFICACION         NUMBER(3)            not null,
   PRECIO               NUMBER(9,2)          not null,
   ESTADO               VARCHAR2(10)         not null,
   constraint PK_ESTAMPA primary key (IDESTAMPA)
);

/*==============================================================*/
/* Index: CREA_FK                                               */
/*==============================================================*/
create index CREA_FK on ESTAMPA (
   IDUSUARIO ASC
);

/*==============================================================*/
/* Index: TIENE_FK                                              */
/*==============================================================*/
create index TIENE_FK on ESTAMPA (
   IDTEMATICA ASC
);

/*==============================================================*/
/* Table: FACTURA                                               */
/*==============================================================*/
create table FACTURA 
(
   CODIGOFACTURA        VARCHAR2(12)         not null,
   IDUSUARIO            VARCHAR2(8)          not null,
   PRECIOFINAL          NUMBER(9,2)          not null,
   NUMDOCUMENTO         NUMBER(10)           not null,
   DIRECCIONENTREGA     VARCHAR2(60)         not null,
   ESTADO               VARCHAR2(20)         not null,
   constraint PK_FACTURA primary key (CODIGOFACTURA)
);

/*==============================================================*/
/* Index: GENERA_FK                                             */
/*==============================================================*/
create index GENERA_FK on FACTURA (
   IDUSUARIO ASC
);

/*==============================================================*/
/* Table: MODELOCAMISETA                                        */
/*==============================================================*/
create table MODELOCAMISETA 
(
   IDMODELOCAMISETA     VARCHAR2(10)         not null,
   MODELO               VARCHAR2(10)         not null,
   PRECIO               NUMBER(9,2)          not null,
   IMAGEN1              CLOB                 not null,
   constraint PK_MODELOCAMISETA primary key (IDMODELOCAMISETA)
);

/*==============================================================*/
/* Table: TALLA                                                 */
/*==============================================================*/
create table TALLA 
(
   IDTALLA              VARCHAR2(3)          not null,
   constraint PK_TALLA primary key (IDTALLA)
);

/*==============================================================*/
/* Table: TEMATICA                                              */
/*==============================================================*/
create table TEMATICA 
(
   IDTEMATICA           VARCHAR2(5)          not null,
   NOMBRE               VARCHAR2(30)         not null,
   DESCRIPCION          VARCHAR2(100)        not null,
   constraint PK_TEMATICA primary key (IDTEMATICA)
);

/*==============================================================*/
/* Table: TIPOESTAMPA                                           */
/*==============================================================*/
create table TIPOESTAMPA 
(
   IDTIPOESTAMPA        VARCHAR2(7)          not null,
   IDDETALLEFACTURA     VARCHAR2(10)         not null,
   IDESTAMPA            VARCHAR2(6)          not null,
   POSICION             VARCHAR2(10)         not null,
   constraint PK_TIPOESTAMPA primary key (IDTIPOESTAMPA)
);

/*==============================================================*/
/* Index: AGREGA_FK                                             */
/*==============================================================*/
create index AGREGA_FK on TIPOESTAMPA (
   IDDETALLEFACTURA ASC
);

/*==============================================================*/
/* Index: PERTENECE_FK                                          */
/*==============================================================*/
create index PERTENECE_FK on TIPOESTAMPA (
   IDESTAMPA ASC
);

/*==============================================================*/
/* Table: TIPOUSUARIO                                           */
/*==============================================================*/
create table TIPOUSUARIO 
(
   IDTIPOUSUARIO        VARCHAR2(5)          not null,
   NOMBRE               VARCHAR2(30)         not null,
   constraint PK_TIPOUSUARIO primary key (IDTIPOUSUARIO)
);

/*==============================================================*/
/* Table: USUARIO                                               */
/*==============================================================*/
create table USUARIO 
(
   IDUSUARIO            VARCHAR2(8)          not null,
   IDTIPOUSUARIO        VARCHAR2(5)          not null,
   NOMBREUSUARIO        VARCHAR2(30),
   CONTRASENA           VARCHAR2(20)         not null,
   NOMBRES              VARCHAR2(60)         not null,
   APELLIDOS            VARCHAR2(60)         not null,
   CORREO               VARCHAR2(60)         not null,
   TELEFONO             VARCHAR2(10)         not null,
   constraint PK_USUARIO primary key (IDUSUARIO)
);

/*==============================================================*/
/* Index: ES_FK                                                 */
/*==============================================================*/
create index ES_FK on USUARIO (
   IDTIPOUSUARIO ASC
);

alter table DETALLEFACTURA
   add constraint FK_DETALLEF_COMPONE_TALLA foreign key (IDTALLA)
      references TALLA (IDTALLA);

alter table DETALLEFACTURA
   add constraint FK_DETALLEF_CONTIENE_FACTURA foreign key (CODIGOFACTURA)
      references FACTURA (CODIGOFACTURA);

alter table DETALLEFACTURA
   add constraint FK_DETALLEF_ESPECIFIC_MODELOCA foreign key (IDMODELOCAMISETA)
      references MODELOCAMISETA (IDMODELOCAMISETA);

alter table ESTAMPA
   add constraint FK_ESTAMPA_CREA_USUARIO foreign key (IDUSUARIO)
      references USUARIO (IDUSUARIO);

alter table ESTAMPA
   add constraint FK_ESTAMPA_TIENE_TEMATICA foreign key (IDTEMATICA)
      references TEMATICA (IDTEMATICA);

alter table FACTURA
   add constraint FK_FACTURA_GENERA_USUARIO foreign key (IDUSUARIO)
      references USUARIO (IDUSUARIO);

alter table TIPOESTAMPA
   add constraint FK_TIPOESTA_AGREGA_DETALLEF foreign key (IDDETALLEFACTURA)
      references DETALLEFACTURA (IDDETALLEFACTURA);

alter table TIPOESTAMPA
   add constraint FK_TIPOESTA_PERTENECE_ESTAMPA foreign key (IDESTAMPA)
      references ESTAMPA (IDESTAMPA);

alter table USUARIO
   add constraint FK_USUARIO_ES_TIPOUSUA foreign key (IDTIPOUSUARIO)
      references TIPOUSUARIO (IDTIPOUSUARIO);
