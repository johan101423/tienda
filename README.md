# Sistema de Gestión de Productos en Python

## Descripción

Este proyecto es un sistema sencillo de gestión de productos desarrollado en Python. Es un programa que se ejecuta en la consola y permite al usuario registrar productos, consultar los productos almacenados y calcular el valor total de la compra realizada.

El programa es una práctica básica de programación que utiliza conceptos importantes de Python como funciones, listas, ciclos `while`, validación de datos y estructuras de control. La información de los productos se guarda en una lista llamada `data_base`. En esta lista, cada producto se almacena como una tupla que contiene tres datos: el nombre del producto, el precio unitario y la cantidad.

El objetivo de este proyecto es entender cómo organizar un programa utilizando varias funciones y cómo validar los datos que el usuario ingresa para evitar errores durante la ejecución.

## Cómo funciona

1. Cuando el programa inicia, se muestra un menú con tres opciones principales para el usuario.
2. El usuario debe ingresar un número para seleccionar la opción que desea utilizar.
3. Si el usuario selecciona la opción **1**, el programa solicita el nombre del producto, el precio unitario y la cantidad.
4. Para ingresar los datos, el sistema utiliza funciones de validación que verifican que el usuario escriba información correcta.
5. El nombre del producto se valida para asegurarse de que solo contenga letras.
6. El precio y la cantidad se validan para asegurar que sean números y que no sean valores negativos.
7. Después de ingresar los datos correctamente, el programa crea una tupla con la información del producto.
8. Esta tupla se guarda dentro de la lista `data_base`, que funciona como una pequeña base de datos temporal.
9. Si el usuario selecciona la opción **2**, el programa muestra todos los productos que han sido registrados hasta ese momento.
10. Para cada producto, el sistema muestra el nombre, el precio, la cantidad y el valor total del producto, que se calcula multiplicando el precio por la cantidad.
11. Si el usuario decide finalizar la compra, el programa calcula el valor total de todos los productos almacenados.
12. Finalmente, el sistema muestra el valor general de la compra sumando los valores individuales de cada producto.

## Estado del proyecto
> Este proyecto es un programa educativo y se encuentra en una etapa básica de desarrollo. Actualmente funciona como una herramienta de práctica para aprender Python, especialmente en temas como validación de datos, uso de funciones y manejo de listas.
