import ipaddress
import tkinter as tk
from tkinter import messagebox

def calculate_network_details():
    try:
        # Obtener entrada del usuario
        cidr = entry.get().strip()

        # Crear una red a partir de la entrada
        network = ipaddress.ip_network(cidr, strict=False)

        # Calcular detalles
        netmask = network.netmask
        total_hosts = network.num_addresses
        usable_hosts = total_hosts - 2 if total_hosts > 2 else 0
        network_id = network.network_address
        broadcast_address = network.broadcast_address

        # Mostrar resultados
        result = (f"Máscara de red: {netmask}\n"
                  f"Total de hosts posibles: {total_hosts}\n"
                  f"Total de hosts utilizables: {usable_hosts}\n"
                  f"Network ID: {network_id}\n"
                  f"Dirección de Broadcast: {broadcast_address}")
        messagebox.showinfo("Resultados", result)

    except ValueError:
        messagebox.showerror("Error", "Entrada inválida. Asegúrate de usar el formato correcto (ejemplo: 192.168.1.0/24).")

def create_gui():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Calculadora de Redes")
    root.geometry("600x400")
    root.configure(bg="black")

    # Etiqueta de título
    title_label = tk.Label(root, text="Calculadora de Redes", font=("Courier", 18, "bold"), fg="green", bg="black")
    title_label.pack(pady=20)

    # Campo de entrada
    global entry
    entry = tk.Entry(root, font=("Courier", 14), bg="black", fg="green", insertbackground="green")
    entry.pack(pady=10, ipady=5, ipadx=5)
    entry.insert(0, "192.168.1.0/24")

    # Botón para calcular
    calculate_button = tk.Button(root, text="Calcular", font=("Courier", 14), bg="green", fg="black", command=calculate_network_details)
    calculate_button.pack(pady=10)

    # Etiqueta de autor
    author_label = tk.Label(root, text="Creado por 3rrubyCr4ck", font=("Courier", 10), fg="green", bg="black")
    author_label.pack(side="bottom", pady=10)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    create_gui()
