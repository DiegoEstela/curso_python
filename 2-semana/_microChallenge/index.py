""" Deberás crear un diccionario que almacene a los ganadores de la Copa Mundial de la FIFA desde el año 1990 al 2018. Agregar 2022 con Argentina y mostrar el diccionario modificado por pantalla.
Datos para la resolución:

1990 Alemania
1994 Brasil
1998 Francia
2002 Brasil
2006 Italia
2010 España
2014 Alemania
2018 Francia """

mundiales = {
    1990: 'Alemania',
    1994: 'Brasil',
    1998: 'Francia',
    2002: 'Brasil',
    2006: 'Italia',
    2010: 'España',
    2014: 'Alemania',
    2018: 'Francia'
}
mundiales[2022] = 'Argentina'
print(mundiales)
