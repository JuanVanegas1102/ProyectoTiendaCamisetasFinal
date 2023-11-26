-- Introducir valores de Tallas

insert into talla values('XS');
insert into talla values('S');
insert into talla values('M');
insert into talla values('L');
insert into talla values('XL');

-- Introducir tipos de usuario

insert into tipoUsuario values('001','Administrador');
insert into tipoUsuario values('002','Artista');

-- Se inserta usuario de Prueba

insert into usuario values('1','001','Juanito1102','admin','Juan Esteban','Vanegas Rodriguez','juantheboss3@gmail.com','1234512345');
insert into usuario values('2','002','DaVinciArtist','12345','Leonardo','DaVinci','leonardo1@gmail.com','3112252521');

-- Se insertan tematicas para las estampas

insert into tematica values('001','Navidad','Relacionados con la festividad de fin de año, donde se dan regalos y se disfruta en familia.');
insert into tematica values('002','Halloween','Es tiempo del miedo, lo escalofriante y la temporada donde lo paranormal se hace presente.');
insert into tematica values('003','Escolar','Regresa a tu colegio con el mejor estilo.');
insert into tematica values('004','Aesthetic','Minimalista pero original, la moda que ha surgido en los ultimos años.');
insert into tematica values('005','Verano','Disfrutar del sol radiante y la playa, mientras te tomas un refresco y disfrutas del viento.');
insert into tematica values('006','Ink-art','Al estilo clasico, blanco y negro, con diferentes estilos de silueta.');


-- Se insertan materiales para las camisetas

insert into material values('ALG','Algodon');
insert into material values('LAN','Lana');
insert into material values('POL','Poliester');
insert into material values('PAL','Polialgodon');


-- Se insertan modelos de camisetas para el estampado

insert into modelocamiseta values('CAM001','ALG','Cuello-V','https://mackweldon.com/cdn/shop/products/M00T09-BW_Front_0bd51792-7784-46d2-85c0-83e0e62f1a00.png','80',to_date('24/06/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM002','LAN','Cuello-V','https://mackweldon.com/cdn/shop/products/M00T09-BW_Front_0bd51792-7784-46d2-85c0-83e0e62f1a00.png','200',to_date('25/12/2023','dd/mm/yyyy'));
insert into modelocamiseta values('CAM003','POL','Cuello-V','https://mackweldon.com/cdn/shop/products/M00T09-BW_Front_0bd51792-7784-46d2-85c0-83e0e62f1a00.png','320',to_date('01/01/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM004','PAL','Cuello-V','https://mackweldon.com/cdn/shop/products/M00T09-BW_Front_0bd51792-7784-46d2-85c0-83e0e62f1a00.png','120',to_date('16/01/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM005','ALG','MangaLarga','https://madeblanks.com/cdn/shop/products/GYMCLASSLONGSLEEVE_WHITE_0042_WEB.png','100',to_date('11/02/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM006','LAN','MangaLarga','https://madeblanks.com/cdn/shop/products/GYMCLASSLONGSLEEVE_WHITE_0042_WEB.png','200',to_date('02/07/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM007','POL','MangaLarga','https://madeblanks.com/cdn/shop/products/GYMCLASSLONGSLEEVE_WHITE_0042_WEB.png','300',to_date('11/01/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM008','PAL','MangaLarga','https://madeblanks.com/cdn/shop/products/GYMCLASSLONGSLEEVE_WHITE_0042_WEB.png','400',to_date('01/02/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM009','ALG','Tirantes','https://www.blacksocks.com/files/Colette_weiss_web.png','50',to_date('03/01/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM010','LAN','Tirantes','https://www.blacksocks.com/files/Colette_weiss_web.png','30',to_date('01/12/2023','dd/mm/yyyy'));
insert into modelocamiseta values('CAM011','POL','Tirantes','https://www.blacksocks.com/files/Colette_weiss_web.png','130',to_date('20/12/2023','dd/mm/yyyy'));
insert into modelocamiseta values('CAM012','PAL','Tirantes','https://www.blacksocks.com/files/Colette_weiss_web.png','90',to_date('30/12/2023','dd/mm/yyyy'));
insert into modelocamiseta values('CAM013','ALG','Raglan','https://www.tmaker.my/wp-content/uploads/2016/06/76700-white.png','400',to_date('03/01/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM014','LAN','Raglan','https://www.tmaker.my/wp-content/uploads/2016/06/76700-white.png','250',to_date('01/02/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM015','POL','Raglan','https://www.tmaker.my/wp-content/uploads/2016/06/76700-white.png','100',to_date('16/01/2024','dd/mm/yyyy'));
insert into modelocamiseta values('CAM016','PAL','Raglan','https://www.tmaker.my/wp-content/uploads/2016/06/76700-white.png','120',to_date('25/12/2023','dd/mm/yyyy'));


-- Se inserta estampa de prueba

insert into estampa values('EST001','2','004','CartoonDinosaur','Estampado inferior de ocho amigos dinosaurios de colores, felices celebrando.','https://m.media-amazon.com/images/I/81+zgyEJyPL._AC_SY550_.jpg','https://m.media-amazon.com/images/I/61gadxDE06L._AC_SY550_.jpg','https://m.media-amazon.com/images/I/81LdwAo82JL._AC_SY550_.jpg','75','57000.00','Activo');
insert into estampa values('EST002','2','004','Cute Cats','Estampado inferior de gatos de diferentes colores, al estilo de dibujo japones.','https://i.etsystatic.com/37938789/r/il/82fa06/5365543797/il_794xN.5365543797_suzu.jpg','https://i.etsystatic.com/37938789/r/il/66e35a/5317370070/il_794xN.5317370070_cco9.jpg','https://i.etsystatic.com/37938789/r/il/2aaa16/5317370102/il_794xN.5317370102_sbnc.jpg','90','80000.50','Activo');

commit;