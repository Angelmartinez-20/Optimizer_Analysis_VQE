from qiskit.circuit.library import EfficientSU2

num_qubits = int(input("Enter the number of qubits: "))
entanglements = ["linear", "full"]

# Displays 2 types of Circuits #
for entanglement in entanglements:
    form = EfficientSU2(num_qubits = num_qubits, entanglement = entanglement)
    print(f"{entanglement} entanglement:")
    display(form.decompose().draw(fold=-1))