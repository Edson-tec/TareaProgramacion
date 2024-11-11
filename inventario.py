import tkinter as tk
from tkinter import messagebox
from producto import Producto
from excepciones import CantidadInvalidaException, PrecioInvalidoException, ProductoInvalidoException

producto = None

def registrar_producto():
    global producto  
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())
        producto = Producto(nombre, precio, cantidad)
        status.config(text="Producto agregado correctamente", fg="#4CAF50")  # Verde éxito
        detalles_label.config(text="")  # Limpia los detalles previos
    except (ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException) as e:
        status.config(text=f"Error: {str(e)}", fg="#F44336")  # Rojo error
        detalles_label.config(text="PRODUCTO NO VÁLIDO")
    except ValueError:
        status.config(text="Error: Precio y cantidad deben ser números válidos.", fg="#F44336")
        detalles_label.config(text="PRODUCTO NO VÁLIDO")
    except Exception as e:
        status.config(text=f"Error: Ha ocurrido un error: {str(e)}", fg="#F44336")
        detalles_label.config(text="PRODUCTO NO VÁLIDO")

def mostrar_detalles():
    if producto is not None:
        # Muestra los detalles del producto en varias líneas
        detalles_text = (
            f"Nombre: {producto.nombre}\n"
            f"Precio: ${producto.precio:.2f}\n"
            f"Cantidad en inventario: {producto.cantidad}\n"
            f"Valor total en inventario: ${producto.calcular_valor_total():.2f}"
        )
        detalles_label.config(text=detalles_text, fg="#03A9F4")
    else:
        status.config(text="Error: No se ha registrado ningún producto.", fg="#F44336")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("TIENDA")
ventana.geometry("400x500")
ventana.configure(bg="#2C2C2C")  # Fondo gris oscuro

# Encabezado
label_tienda = tk.Label(
    ventana, text="GESTIÓN DE PRODUCTOS", bg="#424242", fg="#E0E0E0",
    font=("Arial", 18, "bold"), relief="ridge", highlightbackground="#E0E0E0",
    highlightthickness=2, padx=10, pady=10
)
label_tienda.pack(pady=10)

# Nombre del producto
label_nombre = tk.Label(
    ventana, text="Nombre del producto:", bg="#2C2C2C", fg="#B0BEC5",
    font=("Arial", 12)
)
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, bg="#CFD8DC", font=("Arial", 12))
entry_nombre.pack(pady=5)

# Precio del producto
label_precio = tk.Label(
    ventana, text="Precio del producto:", bg="#2C2C2C", fg="#B0BEC5",
    font=("Arial", 12)
)
label_precio.pack(pady=5)
entry_precio = tk.Entry(ventana, bg="#CFD8DC", font=("Arial", 12))
entry_precio.pack(pady=5)

# Cantidad en inventario
label_cantidad = tk.Label(
    ventana, text="Cantidad en inventario:", bg="#2C2C2C", fg="#B0BEC5",
    font=("Arial", 12)
)
label_cantidad.pack(pady=5)
entry_cantidad = tk.Entry(ventana, bg="#CFD8DC", font=("Arial", 12))
entry_cantidad.pack(pady=5)

# Frame para alinear los botones en una fila
button_frame = tk.Frame(ventana, bg="#2C2C2C")
button_frame.pack(pady=10)

# Botón para registrar el producto
boton_registrar = tk.Button(
    button_frame, text="Registrar", command=registrar_producto,
    fg="#FFFFFF", bg="#2196F3", font=("Arial", 10), width=15, relief="raised", padx=2, pady=2
)
boton_registrar.grid(row=0, column=0, padx=5)

# Botón para mostrar los detalles del producto
boton_mostrar = tk.Button(
    button_frame, text="Mostrar", command=mostrar_detalles,
    fg="#FFFFFF", bg="#009688", font=("Arial", 10), width=15, relief="raised", padx=2, pady=2
)
boton_mostrar.grid(row=0, column=1, padx=5)

# Área de mensajes de estado y detalles del producto
status = tk.Label(ventana, text="", fg="#F44336", bg="#2C2C2C", font=("Arial", 10), relief="sunken")
status.pack(pady=5)
detalles_label = tk.Label(ventana, text="", fg="#03A9F4", bg="#2C2C2C", font=("Arial", 10), relief="sunken", justify="left")
detalles_label.pack(pady=5)

# Iniciar el loop de la aplicación
ventana.mainloop()
