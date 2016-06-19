#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 29-04-2016

@author: leonardojofre
'''

from selenium import webdriver
from selenium.webdriver.support.select import Select



titulo = """
CLASES de ESTADISTICA e INFERENCIA, Trabajos y APOYO ONLINE
"""
texto = u"""
Realizo Clases Particulares a Domicilio en Santiago y On-Line a Regiones, Desarrollo de Trabajos y APOYO On-Line para Universitarios Diurnos y Vespertinos, Educación Técnica Superior y Educación media.

Clases particulares on-line, resuelve tus dudas con materia específica que no entiendas y resuelve ejercicios paso a paso, explicación de teoría y aplicación.

Soy Egresada de Ingeniería Industrial mas de 4 años como Ayudante en universidad e Institutos y Profesora Particular Educación media a superior. Metodología orientada a todas las carreras y distintos niveles de profundidad. Experiencia con alumnos de diferentes universidades e institutos. Coordina con tiempo y salva tu ramo.

***TRABAJOS - TAREAS - Desarrollo GUÍAS paso a paso - APOYO ON-LINE***

Valor Clase presencial: $10.000 (una hora)
Valor Clase on-line: $12.000 (una hora y 30 minutos)
VALOR Trabajos y Tareas: $15.000 (DESDE)

Disponibilidad de Lunes a Domingo
A Domicilio o lugar a convenir en Santiago
Clases on-line para Santiago y Regiones

CONTACTO: Fono whatsapp: +5697 956 8119

ASIGNATURAS / RAMOS:

*** ESTADÍSTICA y Probabilidad (ESTADISTICA 1)

- Estadística Descriptiva, Representación Gráfica, Análisis Bivariado y Correlación.
- Utilización herramientas EXCEL y Programación en R
- Regresión Lineal.
- Probabilidad clásica (espacio muestral, cálculo probabilidad de un evento, probabilidad total, teorema de bayes)
- Variable Aleatoria Discreta y Continua
- Distribuciones de Probabilidad Discretas (Binomial, Poisson, etc)
- Distribuciones de Probabilidad Continuas (Normal, Uniforme, Gama, etc).
( y mas )

*** INFERENCIA ESTADÍSTICA:

- Estimador Máximo Verosímil (y demás métodos)
- INTERVALO DE CONFIANZA una y dos muestras.
- Teorema de Limite central, Error de tipo 1 y 2
- PRUEBA ó DÓCIMA DE HIPÓTESIS Una y Dos muestras.
- ANOVA
- Bondad de Ajuste, pruebas Chi cuadrado

*** ANÁLISIS ESTADÍSTICO
*** CONTROL DE PROCESOS ESTADÍSTICO

Consultar por OTRAS ÁREAS: Nivelación Matemática, Cálculo, Álgebra, Ecuaciones Diferenciales, Física, QUIMICA, Electromagnetismo, INVESTIGACIÓN DE OPERACIONES

Fono whatsapp: +5697 956 8119
----
Saludos Ali.

UCHILE - PUC - USACH – UTFSM – UNAB – U TALCA - UDD - UGM – UAH – UBO –UB – UCINF – UDLA – UST - SEK - DUOC – INACAP - IACC – IPP – AIEP - ICEL
"""
username = "ljofre"
email = 'leonardojofre@aliclass.cl'
password = "Ljofre2146"

url = "http://www.vivastreet.cl/"
mi_cuenta = "http://www.vivastreet.cl/account_classifieds.php"
login_url = 'http://www.vivastreet.cl/login.php'
post_url = "http://post.vivastreet.cl/"

# 'chromedriver' executable needs to be in PATH

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get(url=login_url)

el_email = driver.find_element_by_name('email').send_keys(email)
el_pass = driver.find_element_by_name('password').send_keys(password)
submit = driver.find_element_by_tag_name('input')
submit.submit()

# publicar aviso gratis

driver.find_element_by_id('vs_posting_button').click()
categoria = Select(driver.find_element_by_id('posting_category_select'))
categoria.select_by_visible_text('Clases')

classes_private = filter(lambda x: x.get_attribute('value') == 'classes_private', driver.find_elements_by_name('subcat_select'))[0]
classes_private.click()

postingGeo_1 = Select(driver.find_element_by_id('postingGeo_1'))
postingGeo_1.select_by_value('34')

postingGeo_2 = Select(driver.find_element_by_id('postingGeo_2'))
postingGeo_2.select_by_value('35')

id_individual_type = Select(driver.find_element_by_id('id_individual_type'))
id_individual_type.select_by_value('pro')

# titulo y descripcion
title = driver.find_element_by_id('title')
title.send_keys(titulo)
detail = driver.find_element_by_id('detail')
detail.send_keys(texto)

driver.find_elements_by_tag_name('use')








