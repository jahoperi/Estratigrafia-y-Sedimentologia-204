# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:27:33 2022

@author: jahop_fz60h0
"""

import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests
import plotly.express as px

#import pandas as pd
#import numpy as np

#import plotly.graph_objects as go 


from PIL import Image

image = Image.open('pemex.png')
st.image(image)


    
st.title("Estratigrafía y Sedimentología")
page_names = ['Ada Bolivia Compañ Cadena', 'Adriana Delfina Manrique García', 'Alberto Carlos Manzanilla Vargas', 'Alejandro Rueda Rangel', 'Alfredo Castelo Vázquez', 'Alfredo Rivera Cruz', 'Alicia Rivero Torres', 'Aly Giovanni Morán García', 'Angel Antonio Saldaña Loredo', 'Anselmo Víctor González García', 'Araceli Guillermina Olivera Ortega', 'Baltazar Hernández Sánchez', 'Bernardo Matías Santiago', 'Betsabé Cortés Becerril', 'Brenda Carolina Salinas Castillo', 'Carlos Héctor Del Angel Castillo', 'Carlos Lambarria Silva', 'César Alejandro Bravo Cruz', 'César Arturo Sereno Alvarado', 'César Augusto Cuapio Pérez', 'Clotilde Prieto Ubaldo', 'Damaris Jiménez Bueno', 'Daniel Allen González Becerra', 'Dante Israel Granados Vázquez', 'Diana Irene Salguero Olvera', 'Dora Edith Cruz Marroquín', 'Eduardo Medina Dominguez', 'Edwin Nereo Gómez Hernández', 'Eli Moisés Hernández Diazgirón', 'Elizabeth Reyes George', 'Elizama Requena López', 'Emery Payán Bañales', 'Erick Iturbe Ortiz', 
'Erick Omar Reyes Hernández', 'Erika Beatriz Cano Ibarra', 'Ezequiel Rosas Velázquez', 'Fabián Tizoc Jiménez Berna', 'Fabiola Concepción Cruz Marquez Benítez', 'Federico Felipe Velázquez Castro', 'Felipe de Jesús Lavariega Trujillo', 'Felipe Neri Saldaña Pedraza', 'Fidel Hector Ruiz Ruiz', 'Florencio Aurelio Nava Gordon', 'Francisco Javier Huerta Rosas', 'Francisco Olivares Pérez', 'Gerardo Chávez Vázquez', 'Gilberto Espinoza Crispín', 'Gloria Leticia Flores Acosta', 'Graciela Dolores Ramírez Villaseñor', 'Graciela Esmeralda González Mercado', 'Guadalupe Inés Cruz Antonio', 'Gustavo Bernardo Mellin Patricio', 'Hector Martin Jiménez Marquez', 'Héctor René Delgado González', 'Heriberto Octaviano Turrubiates Becerra', 'Hilda Clarisa Gutiérrez Paredes', 'Humberto Alarcón Sosa', 'Humberto Torres Sastre', 'Iván Guzmán Ibarra', 'Iván Vladimir Villagrana Macías', 'Jerónimo Rodríguez Figueroa', 'Jessica Torres Hernández', 'Jesús Alejandro García Arias', 'Jesús Humberto Salgado Murrieta',
'Joaquín Carbajal Casados', 'Jorge Amado Silva Sosa',	'Jorge Antonio Velasco Segura', 'Jose Adrian Sanchez Lira', 'José Angel Reyes Tovar', 'José Bernardo Vázquez Toledo', 'José de Jesús Vega Carrillo', 'José Francisco Martínez Contreras',	'José Jesús Camacho Vargas', 'José L Posadas Barrios', 'José Manuel Del Moral Domínguez', 'José Manuel Vasconcelos Fernández', 'José Rafael Coronado Peralta', 'José Ramón Bravo Pérez', 'José Ramon Sales Alvarez', 'José Ricardo Villagrán Yáñez', 'Juan Andres García Alvarado', 'Juan Manuel Osorio Hernández', 'Juan Olivares Flores', 'Juana Orquídea Salas Ramírez', 'Julieta Martínez García', 'Karina Uribe Trejo', 'Karla Yadira Castillo Bermudez', 'Leonardo López Sánchez', 'Lidia Alicia Aguirre Meza', 'Lorenzo Alberto Cornelio Rodríguez',	'Lucio Francisco González Gutiérrez', 'Luis Enrique Huerta Páez', 'Luis Lauro Villanueva González', 'Luisa Vara Rubio',	'Luz Angélica Tristán Serrano', 'Luz María Alva Reyes', 'Ma. Julieta Nava Fuentes',
'Manuel Alejandro Mercado Estrada',	'Manuel Felipe Román Zamora', 'Manuel Machorro Jiménez', 'Marco Antonio San Martin Zaleta', 'Maria de los Ángeles Rodríguez Hernández', 'María del Carmen García Rodríguez', 'Maria Eugenia Baltazar Montes', 'María Teresa Landero Reyes', 'Maricela Angulo Hernández', 'Mario Antonio Colunga Osorio', 'Martha Cecilia Madrigal Acosta', 'Martín González Castillo', 'Martín Martínez Medrano', 'Mauricio Israel Galindo Charles', 'Miguel Angel Zaragoza Estrada', 'Miguel Gerardo Tobías Hernández', 'Miguel Mata López', 'Monica Quintanilla Pérez', 'Nancy Edith Gómez Vázquez', 'Nelson Damián Porras Vázquez', 'Nohemí Arteaga Martínez', 'Nora Alicia Marín Matus', 'Nora Rubí Lárraga Bautista', 'Nora Santillán Arriaga', 'Oscar Elorza Martínez', 'Oscar Guadalupe Piñeyro Argüelles', 'Oswaldo Ramírez Martínez', 'Paola Fabiola Sanchez Peña', 'Patricia Hernández Bernal', 'Pedro Junior Cruz Contreras', 'Ramiro Ríos Rojas', 'René Homero Beltrán Ríos', 'Ricardo Sandoval Silva',
'Ricardo Worbis Torres', 'Roberto Cruz Martínez', 'Rubén Ernesto Oviedo Lerma', 'Salvador Morales Soto', 'Saúl Rodríguez Trejo', 'Sergio Beaurregard Beaurregard', 'Sergio Cacho Casillas', 'Sergio Jiménez Magaña', 'Silvia de los Ángeles Padilla Ramos',	'Simeón Oseguera Hernández', 'Víctor Alfonso Martínez Ortega', 'Víctor Antonio Rodríguez Ortiz', 'Víctor Manuel Álvarez Maya', 'Víctor Raul Rodríguez Meneses', 'Xóchitl Morán Federico', 
'Yessika Zurit Pérez Zamudio', 'Unión de los gráficos']

page = st.radio('Navegación', page_names, index = 0)
#st.write("**La variable 'page' returns:**", page)

#df = pd.read_excel("NDR_PC-3.xlsx")
#st.title("Datos")
#st.write(df)


#1 vertical menu

#selected = option_menu(
#    menu_title = "Geología Estructural", #required
#    options = ["Ariel Ramírez Díaz", "Arnulfo Zarate Santiago", "Daniel Gómez Ochoa", "Gustavo Gutiérrez Rodríguez", "Jesica Aguirre Olguin", "Jesús Alejandro García Cantú", "José Luis Landa Mondragon", "María Elena Arenas Martínez", "Marybeth Garrido Hernández", "Mónica Rodríguez Otero", "Nestor Daniel Ortíz Najera", "Oscar Emmanuel Guadalupe Vences Estudillo", "Raúl Arturo Palacios Zamora", "Rosalía Molina Mandujano", "Uriel Román Manjarrez Juárez", "Uzziel Saldaña Hernández", "Verónica Iveth Ramírez Soria", "Yessica Guerrero Amador"], #required
#    #icons = ["house", "envelope", "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope",], #optional
#    #icons = ["house"],
#    menu_icon = "cast", #optional
#    default_index = 0, #optional
    
#    ) 
 

################################################################################################################################################################  
#1                 
if page == 'Ada Bolivia Compañ Cadena':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,4,4,4,4,2,3,3,3,2,4,1,1,2,4,3,3,4,1,5])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ada Bolivia Compañ Cadena', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")
   
#2
if page == 'Adriana Delfina Manrique García':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,2,2,3,3,3,3,2,2,1,2,2,3,2,3,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Adriana Delfina Manrique García', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   

#3
if page == 'Alberto Carlos Manzanilla Vargas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alberto Carlos Manzanilla Vargas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#4
if page == 'Alejandro Rueda Rangel':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,3,3,3,3,3,2,3,2,2,2,2,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alejandro Rueda Rangel', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#5
if page == 'Alfredo Castelo Vázquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alfredo Castelo Vázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#6
if page == 'Alfredo Rivera Cruz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,3,3,2,2,2,1,3,2,2,2,2,2,2,1,3,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alfredo Rivera Cruz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#7
if page == 'Alicia Rivero Torres':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,2,3,2,3,2,3,3,3,3,1,1,2,2,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alicia Rivero Torres', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#8
if page == 'Aly Giovanni Morán García':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,3,3,2,2,2,1,1,1,2,2,2,2,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Aly Giovanni Morán García', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#9
if page == 'Angel Antonio Saldaña Loredo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,2,1,3,1,3,2,2,1,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Angel Antonio Saldaña Loredo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#10
if page == 'Anselmo Víctor González García':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,2,2,2,1,2,3,2,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Anselmo Víctor González García', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
############### 10 ############################################################################################################################################

#11
if page == 'Araceli Guillermina Olivera Ortega':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,3,3,2,2,2,3,3,3,2,2,1,2,2,2,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Araceli Guillermina Olivera Ortega', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#12
if page == 'Baltazar Hernández Sánchez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,5,2,2,2,2,3,3,2,2,2,1,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Baltazar Hernández Sánchez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#13
if page == 'Bernardo Matías Santiago':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,3,3,4,3,3,3,2,1,3,2,4,3,3,3,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Bernardo Matías Santiago', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#14
if page == 'Betsabé Cortés Becerril':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,3,2,2,2,3,2,2,2,1,2,2,2,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Betsabé Cortés Becerril', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#15
if page == 'Brenda Carolina Salinas Castillo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,3,3,2,3,3,2,2,2,2,1,1,1,1,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Brenda Carolina Salinas Castillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#16
if page == 'Carlos Héctor Del Angel Castillo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,2,3,3,3,3,3,4,4,4,2,2,3,3,2,4,3,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Carlos Héctor Del Angel Castillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#17
if page == 'Carlos Lambarria Silva':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,4,4,4,3,4,4,4,3,3,3,2,3,3,3,4,2,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Carlos Lambarria Silva', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#18
if page == 'César Alejandro Bravo Cruz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,2,2,3,2,2,2,1,1,1,1,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='César Alejandro Bravo Cruz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#19
if page == 'César Arturo Sereno Alvarado':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='César Arturo Sereno Alvarado', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#20
if page == 'César Augusto Cuapio Pérez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,2,3,4,3,2,2,2,2,2,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='César Augusto Cuapio Pérez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

############   20  ############################################################################################################################################

#21
if page == 'Clotilde Prieto Ubaldo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,2,3,4,3,4,4,2,2,3,3,3,3,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Clotilde Prieto Ubaldo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 
   
#22
if page == 'Damaris Jiménez Bueno':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,2,2,2,1,2,2,2,2,2,1,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Damaris Jiménez Bueno', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#23
if page == 'Daniel Allen González Becerra':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Daniel Allen González Becerra', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#24
if page == 'Dante Israel Granados Vázquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,5,4,4,4,4,4,4,5,4,3,3,4,4,3,4,3,4,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Dante Israel Granados Vázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#25
if page == 'Diana Irene Salguero Olvera':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,3,4,4,3,3,2,3,2,4,2,3,2,3,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Diana Irene Salguero Olvera', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#26
if page == 'Dora Edith Cruz Marroquín':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,2,2,3,3,1,3,2,2,1,1,1,1,1,1,2,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Dora Edith Cruz Marroquín', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#27
if page == 'Eduardo Medina Dominguez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,2,2,3,2,2,2,1,2,1,2,1,3,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Eduardo Medina Dominguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#28
if page == 'Edwin Nereo Gómez Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Edwin Nereo Gómez Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#29
if page == 'Eli Moisés Hernández Diazgirón':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,3,4,4,3,5,4,4,5,4,3,4,3,1,1,1,1,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Eli Moisés Hernández Diazgirón', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#30
if page == 'Elizabeth Reyes George':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Elizabeth Reyes George', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#########  30   ###############################################################################################################################################   
   
#31
if page == 'Elizama Requena López':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,3,3,3,3,3,3,3,3,3,3,1,2,1,1,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Elizama Requena López', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#32
if page == 'Emery Payán Bañales':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,4,4,3,4,4,4,4,5,3,2,3,2,2,3,2,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Emery Payán Bañales', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#33
if page == 'Erick Iturbe Ortiz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,2,3,3,3,2,2,2,2,1,1,1,1,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Erick Iturbe Ortiz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#34
if page == 'Erick Omar Reyes Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,3,3,3,2,1,2,3,1,2,3,2,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Erick Omar Reyes Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#35
if page == 'Erika Beatriz Cano Ibarra':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,3,2,3,3,3,3,2,2,2,2,3,1,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Erika Beatriz Cano Ibarra', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#36
if page == 'Ezequiel Rosas Velázquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ezequiel Rosas Velázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#37
if page == 'Fabián Tizoc Jiménez Berna':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,4,3,2,3,4,3,3,3,3,2,3,2,2,2,3,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Fabián Tizoc Jiménez Berna', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#38
if page == 'Fabiola Concepción Cruz Marquez Benítez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,1,1,2,3,3,2,4,3,2,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Fabiola Concepción Cruz Marquez Benítez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#39
if page == 'Federico Felipe Velázquez Castro':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,3,3,3,2,1,1,1,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Federico Felipe Velázquez Castro', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#40
if page == 'Felipe de Jesús Lavariega Trujillo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,5,2,4,2,3,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Felipe de Jesús Lavariega Trujillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
##########  40   ############################################################################################################################################   
   
#41
if page == 'Felipe Neri Saldaña Pedraza':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,4,3,4,4,4,4,3,3,2,2,2,2,3,3,2,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Felipe Neri Saldaña Pedraza', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#42
if page == 'Fidel Hector Ruiz Ruiz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,1,4,4,2,3,4,2,4,4,2,1,3,2,1,2,3,3,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Fidel Hector Ruiz Ruiz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#43
if page == 'Florencio Aurelio Nava Gordon':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,1,2,3,2,2,3,2,3,2,2,1,1,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Florencio Aurelio Nava Gordon', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#44
if page == 'Francisco Javier Huerta Rosas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,3,1,1,2,2,2,2,1,1,1,1,1,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Francisco Javier Huerta Rosas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#45
if page == 'Francisco Olivares Pérez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,4,3,4,4,4,3,4,2,3,3,2,3,3,3,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Francisco Olivares Pérez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#46
if page == 'Gerardo Chávez Vázquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,1,2,3,2,2,3,2,2,1,1,3,3,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gerardo Chávez Vázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#47
if page == 'Gilberto Espinoza Crispín':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gilberto Espinoza Crispín', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#48
if page == 'Gloria Leticia Flores Acosta':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,3,2,3,2,2,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gloria Leticia Flores Acosta', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#49
if page == 'Graciela Dolores Ramírez Villaseñor':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,4,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Graciela Dolores Ramírez Villaseñor', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#50
if page == 'Graciela Esmeralda González Mercado':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,4,3,2,4,3,3,3,4,3,2,4,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Graciela Esmeralda González Mercado', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
########  50   ###############################################################################################################################################   
   
#51
if page == 'Guadalupe Inés Cruz Antonio':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,2,2,3,2,4,2,3,2,3,3,3,3,4,1,2,2,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Guadalupe Inés Cruz Antonio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#52
if page == 'Gustavo Bernardo Mellin Patricio':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,2,5,5,5,4,5,5,4,4,2,2,2,3,4,4,4,4,1,5])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gustavo Bernardo Mellin Patricio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#53
if page == 'Hector Martin Jiménez Marquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Hector Martin Jiménez Marquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#54
if page == 'Héctor René Delgado González':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,2,3,3,3,3,2,3,2,3,2,1,2,2,1,2,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Héctor René Delgado González', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#55
if page == 'Heriberto Octaviano Turrubiates Becerra':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,3,3,3,4,4,4,3,3,3,3,2,3,3,4,3,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Heriberto Octaviano Turrubiates Becerra', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#56
if page == 'Hilda Clarisa Gutiérrez Paredes':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,3,3,2,4,4,3,2,4,2,3,3,1,1,2,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Hilda Clarisa Gutiérrez Paredes', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#57
if page == 'Humberto Alarcón Sosa':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,4,4,4,2,4,4,3,4,3,3,2,3,3,5,3,5,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Humberto Alarcón Sosa', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#58
if page == 'Humberto Torres Sastre':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,4,2,4,2,3,2,3,1,3,3,1,1,1,1,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Humberto Torres Sastre', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#59
if page == 'Iván Guzmán Ibarra':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,3,3,3,3,3,1,2,2,1,2,2,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Iván Guzmán Ibarra', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#60
if page == 'Iván Vladimir Villagrana Macías':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,2,3,2,2,3,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Iván Vladimir Villagrana Macías', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#####  60  #####################################################################################################################################################   
   
#61
if page == 'Jerónimo Rodríguez Figueroa':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,4,3,4,3,3,2,3,3,3,3,3,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jerónimo Rodríguez Figueroa', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#62
if page == 'Jessica Torres Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,1,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jessica Torres Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    

#63
if page == 'Jesús Alejandro García Arias':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,4,4,4,4,4,5,4,4,3,3,2,4,2,2,3,4,1,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jesús Alejandro García Arias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#64
if page == 'Jesús Humberto Salgado Murrieta':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,4,4,4,4,2,4,3,3,2,4,4,2,3,4,1,3,3,4,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jesús Humberto Salgado Murrieta', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#65
if page == 'Joaquín Carbajal Casados':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,2,2,3,2,2,2,2,2,2,2,1,1,2,1,3,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Joaquín Carbajal Casados', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#66
if page == 'Jorge Amado Silva Sosa':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,2,1,1,1,1,3,2,2,1,3,2,1,1,1,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jorge Amado Silva Sosa', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#67
if page == 'Jorge Antonio Velasco Segura':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,3,2,3,3,3,3,2,3,2,3,2,2,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jorge Antonio Velasco Segura', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#68
if page == 'Jose Adrian Sanchez Lira':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jose Adrian Sanchez Lira', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#69
if page == 'José Angel Reyes Tovar':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,3,2,3,3,3,3,2,2,1,1,2,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Angel Reyes Tovar', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#70
if page == 'José Bernardo Vázquez Toledo':
    #st.title(f"Has seleccionado {selected}")
    fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Bernardo Vázquez Toledo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
    fig.update_yaxes(range = [0,5])
    st.plotly_chart(fig)
    #fig.show()
else:   
    st.subheader("")
    st.write("")   

#########  70  ##############################################################################################################################################    
#71
if page == 'José de Jesús Vega Carrillo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José de Jesús Vega Carrillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()Vanessa del Carmen Farias Couoh
else:   
   st.subheader("")
   st.write("")    
   
#72                 
if page == 'José Francisco Martínez Contreras':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Francisco Martínez Contreras', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")
   
#73
if page == 'José Jesús Camacho Vargas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Jesús Camacho Vargas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   

#74
if page == 'José L Posadas Barrios':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José L Posadas Barrios', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#75
if page == 'José Manuel Del Moral Domínguez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,3,2,3,3,2,1,3,2,2,2,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Manuel Del Moral Domínguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#76
if page == 'José Manuel Vasconcelos Fernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Manuel Vasconcelos Fernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#77
if page == 'José Rafael Coronado Peralta':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,3,2,3,3,3,3,3,2,2,3,2,2,3,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Rafael Coronado Peralta', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#78
if page == 'José Ramón Bravo Pérez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,3,2,3,3,3,3,2,1,1,1,1,2,1,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Ramón Bravo Pérez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#79
if page == 'José Ramon Sales Alvarez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,4,3,4,3,3,3,4,3,2,3,3,4,4,4,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Ramon Sales Alvarez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#80
if page == 'José Ricardo Villagrán Yáñez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,1,3,3,3,3,4,3,2,3,1,1,2,3,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Ricardo Villagrán Yáñez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   

#########  80   ##############################################################################################################################################
   
#81
if page == 'Juan Andres García Alvarado':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,1,3,2,2,2,1,2,1,1,1,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Andres García Alvarado', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#82
if page == 'Juan Manuel Osorio Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,3,4,3,3,3,3,3,3,3,2,3,2,1,1,2,3,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Manuel Osorio Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#83
if page == 'Juan Olivares Flores':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,3,3,2,3,3,3,3,3,3,2,2,2,2,3,3,3,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Olivares Flores', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#84
if page == 'Juana Orquídea Salas Ramírez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,2,2,3,3,2,3,3,2,1,1,1,4,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juana Orquídea Salas Ramírez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#85
if page == 'Julieta Martínez García':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,2,3,3,3,3,3,3,3,3,3,1,2,1,1,3,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Julieta Martínez García', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#86
if page == 'Karina Uribe Trejo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,2,3,3,3,4,3,2,1,2,2,1,1,1,3,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Karina Uribe Trejo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#87
if page == 'Karla Yadira Castillo Bermudez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,3,1,3,1,2,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Karla Yadira Castillo Bermudez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#88
if page == 'Leonardo López Sánchez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,3,2,3,2,3,2,3,2,2,2,2,2,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Leonardo López Sánchez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#89
if page == 'Lidia Alicia Aguirre Meza':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,2,1,1,1,2,2,2,1,1,2,1,1,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lidia Alicia Aguirre Meza', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#90
if page == 'Lorenzo Alberto Cornelio Rodríguez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,3,1,3,2,2,2,1,2,3,1,3,3,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lorenzo Alberto Cornelio Rodríguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#######  90 ###################################################################################################################################################

#91
if page == 'Lucio Francisco González Gutiérrez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,3,3,3,3,3,3,3,2,2,1,1,2,3,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lucio Francisco González Gutiérrez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#92
if page == 'Luis Enrique Huerta Páez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,5,4,4,4,2,4,4,4,4,4,3,1,4,1,1,3,3,4,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luis Enrique Huerta Páez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 
   
#93
if page == 'Luis Lauro Villanueva González':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,5,4,5,5,3,4,5,4,4,4,3,2,4,2,4,3,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luis Lauro Villanueva González', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#94
if page == 'Luisa Vara Rubio':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,4,3,2,2,2,2,3,2,2,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luisa Vara Rubio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#95
if page == 'Luz Angélica Tristán Serrano':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,4,4,4,3,4,4,4,3,3,3,3,4,3,2,3,3,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luz Angélica Tristán Serrano', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#96
if page == 'Luz María Alva Reyes':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,2,2,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luz María Alva Reyes', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#97
if page == 'Ma. Julieta Nava Fuentes':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,1,2,3,2,2,2,2,2,2,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ma. Julieta Nava Fuentes', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#98
if page == 'Manuel Alejandro Mercado Estrada':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,1,2,1,2,1,3,1,2,1,2,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Manuel Alejandro Mercado Estrada', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#99
if page == 'Manuel Felipe Román Zamora':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,2,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Manuel Felipe Román Zamora', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#100
if page == 'Manuel Machorro Jiménez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,4,3,3,3,3,4,4,4,4,4,2,2,4,2,2,3,2,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Manuel Machorro Jiménez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    

#######  100   ###############################################################################################################################################
   
#101
if page == 'Marco Antonio San Martin Zaleta':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,3,3,2,2,2,2,2,3,3,1,3,1,1,1,1,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Marco Antonio San Martin Zaleta', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#102
if page == 'Maria de los Ángeles Rodríguez Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,3,4,4,4,2,4,4,3,4,4,2,3,4,2,2,3,3,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Maria de los Ángeles Rodríguez Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#103
if page == 'María del Carmen García Rodríguez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,4,4,2,4,4,3,3,2,2,3,3,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María del Carmen García Rodríguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#104
if page == 'Maria Eugenia Baltazar Montes':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,3,3,3,2,2,2,3,3,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Maria Eugenia Baltazar Montes', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#105
if page == 'María Teresa Landero Reyes':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María Teresa Landero Reyes', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#106
if page == 'Maricela Angulo Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Maricela Angulo Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#107
if page == 'Mario Antonio Colunga Osorio':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Mario Antonio Colunga Osorio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#108
if page == 'Martha Cecilia Madrigal Acosta':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Martha Cecilia Madrigal Acosta', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#109
if page == 'Martín González Castillo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,4,3,4,3,4,4,5,5,3,3,3,4,3,3,3,3,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Martín González Castillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#110
if page == 'Martín Martínez Medrano':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,4,3,3,2,4,4,4,4,4,3,2,3,3,3,3,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Martín Martínez Medrano', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     

####  110   ################################################################################################################################################
   
#111
if page == 'Mauricio Israel Galindo Charles':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,5,5,5,5,5,4,5,5,5,5,4,5,4,4,5,5,4,4,5])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Mauricio Israel Galindo Charles', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#112
if page == 'Miguel Angel Zaragoza Estrada':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,2,3,2,1,1,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Miguel Angel Zaragoza Estrada', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#113
if page == 'Miguel Gerardo Tobías Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Miguel Gerardo Tobías Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#114
if page == 'Miguel Mata López':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,3,2,3,3,3,2,3,3,2,3,4,3,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Miguel Mata López', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#115
if page == 'Monica Quintanilla Pérez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Monica Quintanilla Pérez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#116
if page == 'Nancy Edith Gómez Vázquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,3,3,3,2,2,3,3,2,3,2,1,2,1,1,2,1,3,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nancy Edith Gómez Vázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#117
if page == 'Nelson Damián Porras Vázquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nelson Damián Porras Vázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#118
if page == 'Nohemí Arteaga Martínez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nohemí Arteaga Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#119
if page == 'Nora Alicia Marín Matus':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,3,2,4,2,3,2,2,2,2,2,2,2,2,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nora Alicia Marín Matus', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#120
if page == 'Nora Rubí Lárraga Bautista':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,2,2,3,2,3,2,3,1,2,2,1,1,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nora Rubí Lárraga Bautista', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   

#####  120  ##################################################################################################################################################
   
#121
if page == 'Nora Santillán Arriaga':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,1,2,1,2,2,2,2,1,1,1,1,1,2,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nora Santillán Arriaga', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#122
if page == 'Oscar Elorza Martínez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2
])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Oscar Elorza Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#123
if page == 'Oscar Guadalupe Piñeyro Argüelles':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,3,4,5,2,5,4,4,3,4,3,1,3,1,3,2,3,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Oscar Guadalupe Piñeyro Argüelles', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#124
if page == 'Oswaldo Ramírez Martínez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,1,2,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Oswaldo Ramírez Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#125
if page == 'Paola Fabiola Sanchez Peña':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,2,1,2,1,1,1,1,1,1,1,2,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Paola Fabiola Sanchez Peña', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#126
if page == 'Patricia Hernández Bernal':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,2,2,2,2,2,2,2,3,2,2,1,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Patricia Hernández Bernal', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#127
if page == 'Pedro Junior Cruz Contreras':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,3,3,3,3,2,2,3,2,2,2,3,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Pedro Junior Cruz Contreras', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#128
if page == 'Ramiro Ríos Rojas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,2,5,5,2,4,4,4,3,3,3,2,3,1,2,3,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ramiro Ríos Rojas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#129
if page == 'René Homero Beltrán Ríos':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,2,3,3,3,3,3,3,4,3,3,2,3,2,2,3,2,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='René Homero Beltrán Ríos', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:
   st.subheader("")
   st.write("")     
   
#130
if page == 'Ricardo Sandoval Silva':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,2,3,3,3,3,3,2,1,2,1,1,1,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ricardo Sandoval Silva', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     

##### 130  ###################################################################################################################################################
   
#131
if page == 'Ricardo Worbis Torres':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,2,2,2,3,2,2,2,1,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ricardo Worbis Torres', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#132
if page == 'Roberto Cruz Martínez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,2,3,2,3,2,3,3,3,2,1,1,3,1,2,4,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Roberto Cruz Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#133
if page == 'Rubén Ernesto Oviedo Lerma':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,3,3,2,3,3,3,4,4,3,2,1,2,3,3,3,3,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Rubén Ernesto Oviedo Lerma', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    

#134
if page == 'Salvador Morales Soto':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,2,2,1,2,2,1,2,2,1,1,2,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Salvador Morales Soto', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#135
if page == 'Saúl Rodríguez Trejo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,4,3,3,4,3,4,4,4,3,3,2,3,2,3,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Saúl Rodríguez Trejo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#136
if page == 'Sergio Beaurregard Beaurregard':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,1,2,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Sergio Beaurregard Beaurregard', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#137
if page == 'Sergio Cacho Casillas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,1,1,2,2,2,3,1,1,1,1,1,1,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Sergio Cacho Casillas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#138
if page == 'Sergio Jiménez Magaña':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,2,2,2,2,1,2,2,2,2,1,1,1,1,1,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Sergio Jiménez Magaña', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#139
if page == 'Silvia de los Ángeles Padilla Ramos':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,1,2,3,3,3,2,3,3,3,2,2,3,1,1,1,1,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Silvia de los Ángeles Padilla Ramos', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#140
if page == 'Simeón Oseguera Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,1,3,3,3,3,3,2,2,2,3,3,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Simeón Oseguera Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#####   140   ################################################################################################################################################   
#141
if page == 'Víctor Alfonso Martínez Ortega':
    #st.title(f"Has seleccionado {selected}")
    fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,5,1,1,2,1,1,2,3,1,1,2,1,2,1,1,1,1,1,1])
    fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Víctor Alfonso Martínez Ortega', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
    fig.update_yaxes(range = [0,5])
    st.plotly_chart(fig)
    #fig.show()
else:   
    st.subheader("")
    st.write("")   
   
#142
if page == 'Víctor Antonio Rodríguez Ortiz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,3,3,3,3,4,3,3,2,3,1,1,1,1,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Víctor Antonio Rodríguez Ortiz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()Vanessa del Carmen Farias Couoh
else:   
   st.subheader("")
   st.write("")    
   
#143
if page == 'Víctor Manuel Álvarez Maya':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,3,3,1,4,1,4,1,2,2,3,2,3,1,2,4,3,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Víctor Manuel Álvarez Maya', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#144
if page == 'Víctor Raul Rodríguez Meneses':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,3,3,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Víctor Raul Rodríguez Meneses', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#145
if page == 'Xóchitl Morán Federico':
    #st.title(f"Has seleccionado {selected}")
    fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,4,4,2,3,4,4,3,3,2,2,3,2,2,3,2,2,3])
    fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Xóchitl Morán Federico', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
    fig.update_yaxes(range = [0,5])
    st.plotly_chart(fig)
    #fig.show()
else:   
    st.subheader("")
    st.write("")   
   
#146
if page == 'Yessika Zurit Pérez Zamudio':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,1,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Yessika Zurit Pérez Zamudio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()Vanessa del Carmen Farias Couoh
else:   
   st.subheader("")
   st.write("")    
   
########    146     ########################################################################################################################################


    
if page == 'Unión de los gráficos':
     fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,3,2,2,2,1,1,2,2,1,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias',  autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#1                 
     fig.add_scatter(name = 'Ada Bolivia Compañ Cadena',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,4,4,4,4,2,3,3,3,2,4,1,1,2,4,3,3,4,1,5])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

   
#2

     fig.add_scatter(name = 'Adriana Delfina Manrique García',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,2,2,3,3,3,3,2,2,1,2,2,3,2,3,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    

#3
     fig.add_scatter(name = 'Alberto Carlos Manzanilla Vargas',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#4
     fig.add_scatter(name = 'Alejandro Rueda Rangel',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,3,3,3,3,3,2,3,2,2,2,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
   
#5
     fig.add_scatter(name = 'Alfredo Castelo Vázquez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alfredo Castelo Vázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#6
     fig.add_scatter(name = 'Alfredo Rivera Cruz',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,3,3,2,2,2,1,3,2,2,2,2,2,2,1,3,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#7
     fig.add_scatter(name = 'Alicia Rivero Torres',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,2,3,2,3,2,3,3,3,3,1,1,2,2,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#8
     fig.add_scatter(name = 'Aly Giovanni Morán García',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,3,3,2,2,2,1,1,1,2,2,2,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#9
     fig.add_scatter(name = 'Angel Antonio Saldaña Loredo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,2,1,3,1,3,2,2,1,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#10
     fig.add_scatter(name = 'Anselmo Víctor González García',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,2,2,2,1,2,3,2,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
############### 10 ############################################################################################################################################

#11
     fig.add_scatter(name = 'Araceli Guillermina Olivera Ortega',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,3,3,2,2,2,3,3,3,2,2,1,2,2,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#12
     fig.add_scatter(name = 'Baltazar Hernández Sánchez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,5,2,2,2,2,3,3,2,2,2,1,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#13
     fig.add_scatter(name = 'Bernardo Matías Santiago',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,3,3,4,3,3,3,2,1,3,2,4,3,3,3,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#14
     fig.add_scatter(name = 'Betsabé Cortés Becerril',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,3,2,2,2,3,2,2,2,1,2,2,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  

#15
     fig.add_scatter(name = 'Brenda Carolina Salinas Castillo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,3,3,2,3,3,2,2,2,2,1,1,1,1,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#16
     fig.add_scatter(name = 'Carlos Héctor Del Angel Castillo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,2,3,3,3,3,3,4,4,4,2,2,3,3,2,4,3,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    

#17
     fig.add_scatter(name = 'Carlos Lambarria Silva',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,4,4,4,3,4,4,4,3,3,3,2,3,3,3,4,2,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#18
     fig.add_scatter(name = 'César Alejandro Bravo Cruz',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,2,2,3,2,2,2,1,1,1,1,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#19
     fig.add_scatter(name = 'César Arturo Sereno Alvarado',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#20
     fig.add_scatter(name = 'César Augusto Cuapio Pérez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,2,3,4,3,2,2,2,2,2,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

############   20  ############################################################################################################################################

#21
     fig.add_scatter(name = 'Clotilde Prieto Ubaldo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,2,3,4,3,4,4,2,2,3,3,3,3,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#22
     fig.add_scatter(name = 'Damaris Jiménez Bueno',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,2,2,2,1,2,2,2,2,2,1,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#23
     fig.add_scatter(name = 'Daniel Allen González Becerra',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#24
     fig.add_scatter(name = 'Dante Israel Granados Vázquez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,5,4,4,4,4,4,4,5,4,3,3,4,4,3,4,3,4,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#25
     fig.add_scatter(name = 'Diana Irene Salguero Olvera',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,3,4,4,3,3,2,3,2,4,2,3,2,3,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#26
     fig.add_scatter(name = 'Dora Edith Cruz Marroquín',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,2,2,3,3,1,3,2,2,1,1,1,1,1,1,2,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#27
     fig.add_scatter(name = 'Eduardo Medina Dominguez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,2,2,3,2,2,2,1,2,1,2,1,3,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#28
     fig.add_scatter(name = 'Edwin Nereo Gómez Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
#29
     fig.add_scatter(name = 'Eli Moisés Hernández Diazgirón',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,3,4,4,3,5,4,4,5,4,3,4,3,1,1,1,1,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#30
     fig.add_scatter(name = 'Elizabeth Reyes George',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#########  30   ###############################################################################################################################################   
   
#31
     fig.add_scatter(name = 'Elizama Requena López',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,3,3,3,3,3,3,3,3,3,3,1,2,1,1,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#32
     fig.add_scatter(name = 'Emery Payán Bañales',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,4,4,3,4,4,4,4,5,3,2,3,2,2,3,2,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#33
     fig.add_scatter(name = 'Erick Iturbe Ortiz',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,2,3,3,3,2,2,2,2,1,1,1,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#34
     fig.add_scatter(name = 'Erick Omar Reyes Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,3,3,3,2,1,2,3,1,2,3,2,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#35
     fig.add_scatter(name = 'Erika Beatriz Cano Ibarra',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,3,2,3,3,3,3,2,2,2,2,3,1,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Erika Beatriz Cano Ibarra', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#36
     fig.add_scatter(name = 'Ezequiel Rosas Velázquez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#37
     fig.add_scatter(name = 'Fabián Tizoc Jiménez Berna',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,4,3,2,3,4,3,3,3,3,2,3,2,2,2,3,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
        
   
#38
     fig.add_scatter(name = 'Fabiola Concepción Cruz Marquez Benítez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,1,1,2,3,3,2,4,3,2,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
   
#39
     fig.add_scatter(name = 'Federico Felipe Velázquez Castro',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,3,3,3,2,1,1,1,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#40
     fig.add_scatter(name = 'Felipe de Jesús Lavariega Trujillo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,5,2,4,2,3,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
##########  40   ############################################################################################################################################   
   
#41
     fig.add_scatter(name = 'Felipe Neri Saldaña Pedraza',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,4,3,4,4,4,4,3,3,2,2,2,2,3,3,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#42
     fig.add_scatter(name = 'Fidel Hector Ruiz Ruiz',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,1,4,4,2,3,4,2,4,4,2,1,3,2,1,2,3,3,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#43
     fig.add_scatter(name = 'Florencio Aurelio Nava Gordon',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,1,2,3,2,2,3,2,3,2,2,1,1,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
   
#44
     fig.add_scatter(name = 'Francisco Javier Huerta Rosas',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,3,1,1,2,2,2,2,1,1,1,1,1,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#45
     fig.add_scatter(name = 'Francisco Olivares Pérez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,4,3,4,4,4,3,4,2,3,3,2,3,3,3,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#46
     fig.add_scatter(name = 'Gerardo Chávez Vázquez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,1,2,3,2,2,3,2,2,1,1,3,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#47
     fig.add_scatter(name = 'Gilberto Espinoza Crispín',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#48
     fig.add_scatter(name = 'Gloria Leticia Flores Acosta',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,3,2,3,2,2,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#49
     fig.add_scatter(name = 'Graciela Dolores Ramírez Villaseñor',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,4,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#50
     fig.add_scatter(name = 'Graciela Esmeralda González Mercado',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,4,3,2,4,3,3,3,4,3,2,4,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
########  50   ###############################################################################################################################################   
   
#51
     fig.add_scatter(name = 'Guadalupe Inés Cruz Antonio',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,2,2,3,2,4,2,3,2,3,3,3,3,4,1,2,2,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#52
     fig.add_scatter(name = 'Gustavo Bernardo Mellin Patricio',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,2,5,5,5,4,5,5,4,4,2,2,2,3,4,4,4,4,1,5])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#53
     fig.add_scatter(name = 'Hector Martin Jiménez Marquez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#54
     fig.add_scatter(name = 'Héctor René Delgado González',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,2,3,3,3,3,2,3,2,3,2,1,2,2,1,2,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#55
     fig.add_scatter(name = 'Heriberto Octaviano Turrubiates Becerra',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,3,3,3,4,4,4,3,3,3,3,2,3,3,4,3,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#56
     fig.add_scatter(name = 'Hilda Clarisa Gutiérrez Paredes',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,3,3,2,4,4,3,2,4,2,3,3,1,1,2,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#57
     fig.add_scatter(name = 'Humberto Alarcón Sosa',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,4,4,4,2,4,4,3,4,3,3,2,3,3,5,3,5,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#58
     fig.add_scatter(name = 'Humberto Torres Sastre',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,4,2,4,2,3,2,3,1,3,3,1,1,1,1,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#59
     fig.add_scatter(name = 'Iván Guzmán Ibarra',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,3,3,3,3,3,1,2,2,1,2,2,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#60
     fig.add_scatter(name = 'Iván Vladimir Villagrana Macías',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,2,3,2,2,3,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#####  60  #####################################################################################################################################################   
   
#61
     fig.add_scatter(name = 'Jerónimo Rodríguez Figueroa',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,4,3,4,3,3,2,3,3,3,3,3,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#62
     fig.add_scatter(name = 'Jessica Torres Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,1,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      

#63
     fig.add_scatter(name = 'Jesús Alejandro García Arias',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,4,4,4,4,4,5,4,4,3,3,2,4,2,2,3,4,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#64
     fig.add_scatter(name = 'Jesús Humberto Salgado Murrieta',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,4,4,4,4,2,4,3,3,2,4,4,2,3,4,1,3,3,4,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#65
     fig.add_scatter(name = 'Joaquín Carbajal Casados',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,2,2,3,2,2,2,2,2,2,2,1,1,2,1,3,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#66
     fig.add_scatter(name = 'Jorge Amado Silva Sosa',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,2,1,1,1,1,3,2,2,1,3,2,1,1,1,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
   
#67
     fig.add_scatter(name = 'Jorge Antonio Velasco Segura',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,3,2,3,3,3,3,2,3,2,3,2,2,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#68
     fig.add_scatter(name = 'Jose Adrian Sanchez Lira',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
     
#69
     fig.add_scatter(name = 'José Angel Reyes Tovar',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,3,2,3,3,3,3,2,2,1,1,2,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
    
#70
     fig.add_scatter(name = 'José Bernardo Vázquez Toledo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#########  70  ##############################################################################################################################################    
#71
     fig.add_scatter(name = 'José de Jesús Vega Carrillo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#72                 
     fig.add_scatter(name = 'José Francisco Martínez Contreras',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#73
     fig.add_scatter(name = 'José Jesús Camacho Vargas',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    

#74
     fig.add_scatter(name = 'José L Posadas Barrios',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#75
     fig.add_scatter(name = 'José Manuel Del Moral Domínguez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,3,2,3,3,2,1,3,2,2,2,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#76
     fig.add_scatter(name = 'José Manuel Vasconcelos Fernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#77
     fig.add_scatter(name = 'José Rafael Coronado Peralta',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,3,2,3,3,3,3,3,2,2,3,2,2,3,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Rafael Coronado Peralta', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#78
     fig.add_scatter(name = 'José Ramón Bravo Pérez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,3,2,3,3,3,3,2,1,1,1,1,2,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#79
     fig.add_scatter(name = 'José Ramon Sales Alvarez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,3,4,3,4,3,3,3,4,3,2,3,3,4,4,4,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#80
     fig.add_scatter(name = 'José Ricardo Villagrán Yáñez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,1,3,3,3,3,4,3,2,3,1,1,2,3,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     

#########  80   ##############################################################################################################################################
   
#81
     fig.add_scatter(name = 'Juan Andres García Alvarado',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,1,3,2,2,2,1,2,1,1,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#82
     fig.add_scatter(name = 'Juan Manuel Osorio Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,3,4,3,3,3,3,3,3,3,2,3,2,1,1,2,3,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#83
     fig.add_scatter(name = 'Juan Olivares Flores',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,3,3,2,3,3,3,3,3,3,2,2,2,2,3,3,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
#84
     fig.add_scatter(name = 'Juana Orquídea Salas Ramírez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,2,2,3,3,2,3,3,2,1,1,1,4,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
#85
     fig.add_scatter(name = 'Julieta Martínez García',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,2,3,3,3,3,3,3,3,3,3,1,2,1,1,3,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  

#86
     fig.add_scatter(name = 'Karina Uribe Trejo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,2,3,3,3,4,3,2,1,2,2,1,1,1,3,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  

#87
     fig.add_scatter(name = 'Karla Yadira Castillo Bermudez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,3,1,3,1,2,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#88
     fig.add_scatter(name = 'Leonardo López Sánchez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,3,2,3,2,3,2,3,2,2,2,2,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#89
     fig.add_scatter(name = 'Lidia Alicia Aguirre Meza',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,2,1,1,1,2,2,2,1,1,2,1,1,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#90
     fig.add_scatter(name = 'Lorenzo Alberto Cornelio Rodríguez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,3,1,3,2,2,2,1,2,3,1,3,3,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  

#######  90 ###################################################################################################################################################

#91
     fig.add_scatter(name = 'Lucio Francisco González Gutiérrez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,3,3,3,3,3,3,3,2,2,1,1,2,3,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#92
     fig.add_scatter(name = 'Luis Enrique Huerta Páez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,5,4,4,4,2,4,4,4,4,4,3,1,4,1,1,3,3,4,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#93
     fig.add_scatter(name = 'Luis Lauro Villanueva González',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,5,4,5,5,3,4,5,4,4,4,3,2,4,2,4,3,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#94
     fig.add_scatter(name = 'Luisa Vara Rubio',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,4,3,2,2,2,2,3,2,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#95
     fig.add_scatter(name = 'Luz Angélica Tristán Serrano',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,4,4,4,3,4,4,4,3,3,3,3,4,3,2,3,3,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#96
     fig.add_scatter(name = 'Luz María Alva Reyes',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,2,2,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#97
     fig.add_scatter(name = 'Ma. Julieta Nava Fuentes',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,4,1,2,3,2,2,2,2,2,2,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#98
     fig.add_scatter(name = 'Manuel Alejandro Mercado Estrada',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,1,2,1,2,1,3,1,2,1,2,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#99
     fig.add_scatter(name = 'Manuel Felipe Román Zamora',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#100
     fig.add_scatter(name = 'Manuel Machorro Jiménez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,4,3,3,3,3,4,4,4,4,4,2,2,4,2,2,3,2,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      

#######  100   ###############################################################################################################################################
   
#101
     fig.add_scatter(name = 'Marco Antonio San Martin Zaleta',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,3,3,2,2,2,2,2,3,3,1,3,1,1,1,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#102
     fig.add_scatter(name = 'Maria de los Ángeles Rodríguez Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,3,4,4,4,2,4,4,3,4,4,2,3,4,2,2,3,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
        
   
#103
     fig.add_scatter(name = 'María del Carmen García Rodríguez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,4,4,2,4,4,3,3,2,2,3,3,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#104
     fig.add_scatter(name = 'Maria Eugenia Baltazar Montes',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,3,3,3,2,2,2,3,3,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#105
     fig.add_scatter(name = 'María Teresa Landero Reyes',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#106
     fig.add_scatter(name = 'Maricela Angulo Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#107
     fig.add_scatter(name = 'Mario Antonio Colunga Osorio',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#108
     fig.add_scatter(name = 'Martha Cecilia Madrigal Acosta',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
#109
     fig.add_scatter(name = 'Martín González Castillo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,4,3,4,3,4,4,5,5,3,3,3,4,3,3,3,3,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#110
     fig.add_scatter(name = 'Martín Martínez Medrano',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,4,3,3,2,4,4,4,4,4,3,2,3,3,3,3,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    

####  110   ################################################################################################################################################
   
#111
     fig.add_scatter(name = 'Mauricio Israel Galindo Charles',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[5,5,5,5,5,5,4,5,5,5,5,4,5,4,4,5,5,4,4,5])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#112
     fig.add_scatter(name = 'Miguel Angel Zaragoza Estrada',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,2,3,2,1,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#113
     fig.add_scatter(name = 'Miguel Gerardo Tobías Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#114
     fig.add_scatter(name = 'Miguel Mata López',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,3,2,3,3,3,2,3,3,2,3,4,3,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#115
     fig.add_scatter(name = 'Monica Quintanilla Pérez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#116
     fig.add_scatter(name = 'Nancy Edith Gómez Vázquez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,3,3,3,2,2,3,3,2,3,2,1,2,1,1,2,1,3,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#117
     fig.add_scatter(name = 'Nelson Damián Porras Vázquez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nelson Damián Porras Vázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#118
     fig.add_scatter(name = 'Nohemí Arteaga Martínez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nohemí Arteaga Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#119
     fig.add_scatter(name = 'Nora Alicia Marín Matus',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,3,2,4,2,3,2,2,2,2,2,2,2,2,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#120
     fig.add_scatter(name = 'Nora Rubí Lárraga Bautista',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,2,2,3,2,3,2,3,1,2,2,1,1,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   

#####  120  ##################################################################################################################################################
   
#121
     fig.add_scatter(name = 'Nora Santillán Arriaga',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,1,2,1,2,2,2,2,1,1,1,1,1,2,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#122
     fig.add_scatter(name = 'Oscar Elorza Martínez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
#123
     fig.add_scatter(name = 'Oscar Guadalupe Piñeyro Argüelles',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,3,4,5,2,5,4,4,3,4,3,1,3,1,3,2,3,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#124
     fig.add_scatter(name = 'Oswaldo Ramírez Martínez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,1,2,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#125
     fig.add_scatter(name = 'Paola Fabiola Sanchez Peña',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,2,1,2,1,1,1,1,1,1,1,2,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
        
   
#126
     fig.add_scatter(name = 'Patricia Hernández Bernal',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,2,2,2,2,2,2,2,3,2,2,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#127
     fig.add_scatter(name = 'Pedro Junior Cruz Contreras',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,3,3,3,3,2,2,3,2,2,2,3,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#128
     fig.add_scatter(name = 'Ramiro Ríos Rojas',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,2,5,5,2,4,4,4,3,3,3,2,3,1,2,3,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#129
     fig.add_scatter(name = 'René Homero Beltrán Ríos',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,2,3,3,3,3,3,3,4,3,3,2,3,2,2,3,2,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
   
#130
     fig.add_scatter(name = 'Ricardo Sandoval Silva',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,2,3,3,3,3,3,2,1,2,1,1,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
##### 130  ###################################################################################################################################################
   
#131
     fig.add_scatter(name = 'Ricardo Worbis Torres',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,2,2,2,3,2,2,2,1,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
#132
     fig.add_scatter(name = 'Roberto Cruz Martínez',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,2,3,2,3,2,3,3,3,2,1,1,3,1,2,4,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#133
     fig.add_scatter(name = 'Rubén Ernesto Oviedo Lerma',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,3,3,2,3,3,3,4,4,3,2,1,2,3,3,3,3,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    

#134
     fig.add_scatter(name = 'Salvador Morales Soto',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,3,1,2,2,1,2,2,1,2,2,1,1,2,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#135
     fig.add_scatter(name = 'Saúl Rodríguez Trejo',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,4,4,3,3,4,3,4,4,4,3,3,2,3,2,3,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#136
     fig.add_scatter(name = 'Sergio Beaurregard Beaurregard',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,1,2,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
        
   
#137
     fig.add_scatter(name = 'Sergio Cacho Casillas',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,1,1,2,2,2,3,1,1,1,1,1,1,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
   
#138
     fig.add_scatter(name = 'Sergio Jiménez Magaña',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,2,2,2,2,1,2,2,2,2,1,1,1,1,1,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#139
     fig.add_scatter(name = 'Silvia de los Ángeles Padilla Ramos',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,4,1,2,3,3,3,2,3,3,3,2,2,3,1,1,1,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
   
#140
     fig.add_scatter(name = 'Simeón Oseguera Hernández',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,1,3,3,3,3,3,2,2,2,3,3,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#####   140   ################################################################################################################################################   
#14
     fig.add_scatter(name = 'Víctor Alfonso Martínez Ortega',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,5,1,1,2,1,1,2,3,1,1,2,1,2,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
   
#142
     fig.add_scatter(name = 'Víctor Antonio Rodríguez Ortiz',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,3,3,3,3,3,4,3,3,2,3,1,1,1,1,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
  
#143
     fig.add_scatter(name = 'Víctor Manuel Álvarez Maya',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,2,3,3,3,1,4,1,4,1,2,2,3,2,3,1,2,4,3,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
    
   
   
#144
     fig.add_scatter(name = 'Víctor Raul Rodríguez Meneses',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,3,3,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Víctor Raul Rodríguez Meneses', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
   
   
#145
     fig.add_scatter(name = 'Xóchitl Morán Federico',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[4,3,3,4,4,2,3,4,4,3,3,2,2,3,2,2,3,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
      
   
#146
     fig.add_scatter(name = 'Yessika Zurit Pérez Zamudio',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,1,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Yessika Zurit Pérez Zamudio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
   
     st.plotly_chart(fig)
        
else:   
     st.subheader("")
       






    
    
