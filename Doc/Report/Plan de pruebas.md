##Plan de pruebas para DreamsBank
➢**Objetivo de las Pruebas: **
Objetivo general de las pruebas: Verificar la funcionalidad, usabilidad y rendimiento de la aplicación web para proponer proyectos con sus convocatorias y buscar empresas donantes, garantizando que cumpla con los requisitos y expectativas establecidos.
Para lograr este objetivo general, se pueden plantear objetivos específicos adicionales para cubrir diferentes aspectos de la aplicación.




➢**Estrategia de Pruebas:**






|                   | Pruebas Unitarias | Pruebas de Sistema | Pruebas de Aceptación |
|-------------------|-------------------|--------------------|-----------------------|
| Funcionalidad     |         x         |          x         |           x           |
| Usabilidad        |                   |          x         |           x           |
| Mantenibilidad    |         x         |          x         |                       |
| Fiabilidad        |         x         |          x         |                       |




➢**Esquema de Trabajo:**
Se planea realizar pruebas para asegurar el buen funcionamiento del programa, al finalizar se contactará con el cliente para su posterior aprobación.
➢**Herramientas de Apoyo: **
Dentro de las herramientas de software que se utilizaran para llevar a cabo el desarrollo de este plan de pruebas se utilizará: django.test, haciendo uso de los test y de los testing coverage para tomar referencia que porcentaje de las pruebas se han realizado.
➢Tipos Pruebas Aplicar: 
Pruebas de unidad, aceptación, sistemas




➢**Alcance Funcional:**


Gestión de registro de usuario: Este proceso permite a los usuarios registrarse con un perfil dentro de la aplicación. Prueba de unidad.






|                   |  Ingresar datos   | Asignación de categoría|Creación de proyecto |
|-------------------|-------------------|------------------------|---------------------|
| Funcionalidad     |         x         |           x            |          x          |
| Usabilidad        |         x         |                        |          x          |






Gestión de registro de proyecto: Este proceso permite a los admin registrar un proyecto así como asignarle una categoría. Prueba de unidad.








|                   |  Ingresar datos   | Asignación de categoría|Creación de proyecto | Asignación de categoría |
|-------------------|-------------------|------------------------|---------------------|-------------------------|
| Funcionalidad     |         x         |           x            |          x          |            x            |
| Usabilidad        |                   |                        |          x          |                         |








Donación a un proyecto: Este proceso asegura que la donación de una empresa a un proyecto se efectúe de manera efectiva. Prueba de sistemas








|                   |  Identificación del donante   |  Validación de pago  |  Actualización de donación  |
|-------------------|-------------------------------|----------------------|-----------------------------|
| Funcionalidad     |               x               |          x           |              x              |
| Usabilidad        |                               |                      |              x              |




Gestión de registro de categoría: Este proceso debe ayudar a registrar una categoría para categorizar un proyecto. Prueba de unidad








|                   |  Ingresar datos   |  Validación |  Creación de categoría  |
|-------------------|---------------------------------|-------------------------|
| Funcionalidad     |         x         |      x      |           x             |
| Usabilidad        |                   |             |                         |








Gestión de sugerencias:  Este proceso debe asegurar que las sugerencias por los usuarios puedan ser visibles para los programadores del proyecto para ser tenidos en cuenta. Prueba de sistemas








Ingresar 
Validación 




|                   |  Ingresar sugerencia   |  Validación e Identificación  |  Guardado de la sugerencia  |
|-------------------|------------------------|-------------------------------|-----------------------------|
| Funcionalidad     |            x           |               x               |             x               |
| Usabilidad        |            x           |                               |                             |










Experiencia de usuario: Esta prueba se encarga de asegurar una buena experiencia de usuario en la navegabilidad de la aplicación        . Prueba de aceptación










|                   |   Colores intuitivos   |      Validación de pago       |  Actualización de donación  |
|-------------------|------------------------|-------------------------------|-----------------------------|
| Funcionalidad     |            x           |               x               |             x               |
| Usabilidad        |                        |                               |             x               |




Gestión de login y logout: Este proceso se asegura del inicio y cierre de sesión. Prueba de sistemas.




|                   |  Ingresar datos   |  Validación  |  Cierre de sesion  |
|-------------------|-------------------|--------------|--------------------|
| Funcionalidad     |          x        |       x      |         x          |
| Usabilidad        |          x        |              |         x          |




➢**Mecanismos de seguimiento y control:**
El propósito de este oráculo de pruebas es verificar la corrección de las pruebas de unidad y de sistemas realizadas al módulo de knowledge project. Para lograr esto, se han definido dos posibles resultados para cada escenario: éxito y fracaso. En el caso de fracaso, pueden presentarse dos posibilidades: fallo, defecto o errores.
El fallo se refiere a que la prueba fracasó debido a que lo que se está probando no cumple con su función correctamente o incluso no funciona en absoluto. Por otro lado, el defecto se refiere a un error en el código que podría ser un error de sintaxis, problemas de lógica o incluso problemas de diseño.
Por último, se evaluará la calidad del proceso, para lo cual se han definido cuatro atributos o características: corrección, densidad de defectos, confiabilidad y cobertura. Todo lo anterior se llevará a cabo a través de una matriz o tabla que permitirá llevar un seguimiento más organizado de cada iteración.
En la tabla, el campo "prueba" es para el nombre de la prueba y la funcionalidad o módulo. 
El campo "éxito" es para marcar solo si se completó con éxito la prueba, mientras que el campo "fracaso" se marca cuando la prueba falla y se debe registrar el tipo de fracaso junto con una breve descripción de lo que sucedió. 
La correctitud se presenta como un porcentaje y se calcula de la siguiente manera: pruebas exitosas/pruebas ejecutadas.
La densidad de defectos se presenta como un porcentaje y se calcula dividiendo la cantidad de defectos entre la cantidad de casos ejecutados. 
La confiabilidad, por su parte, se calcula de la siguiente manera: (1 - densidad [en decimal])*100. Finalmente, la cobertura se presenta en porcentaje y se calcula dividiendo la cantidad de pruebas ejecutadas entre la cantidad de pruebas planificadas.




| prueba | exito | fracaso | correctitud | densidad defectos | confiabilidad | cobertura |
|             |          |              |                   |                               |                      |                  |