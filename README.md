## Optimization Analysis of the Variational Quantum Eigensolver (VQE)

The VQE is a hybrid algorithm that uses both classical and quantum computers. 
It can solve optimization problems by finding the minimum eigenvalue within a parameter space. 
In this project, it is used to find the minimum energy of a molecule. There are many type of 
optimizers that the algorithm can use. It also iterates the results of the quantum circuit through the 
optimizer and back. Therefore, I conducted an optimization analysis on different optimizers and determined 
how many number of iterations are needed for maximum accuracy.

The `Molecular_Simulation` Folder contains all the source code utilized for simulating molecules. It uses 
Python v3.10.8 and Qiskit v0.46. The `quantum_circuit.py` file prompts the user for a number of qubits and 
illustrates how the quantum circuit would appear within the VQE algorithm.

The `Optimization_Analysis_VQE.pdf` is a research paper encapsulating my findings. It provides a comprehensive explanation 
of the algorithm and presents my research analysis conducted on various optimizers. This paper was submitted to the
CSCSU 2024 Conference, where it was accepted and published. Additionally, the `Poster.pdf` file serves as a summary overview of my work.
