## Optimization Analysis of the Variational Quantum Eigensolver (VQE)

The Variational Quantum Eigensolver (VQE) is a hybrid algorithm that harnesses both classical and quantum computing power. 
It is proficient in solving optimization problems, particularly in this project, where it is employed to determine the 
minimum energy state of a molecule. Various types of optimizers are employed within the algorithm, iterating the 
results of the quantum circuit through these optimizers. Hence, I conducted an optimization analysis on different optimizers 
to ascertain the optimal number of iterations required for maximum accuracy.

The `Molecular_Simulation` Folder contains all the source code utilized for simulating molecules, employing 
Python v3.10.8 and Qiskit v0.46. The `quantum_circuit.py` file prompts the user for the number of qubits and 
illustrates how the quantum circuit would appear within the VQE algorithm.

The `Optimization_Analysis_VQE.pdf` is a research paper encapsulating my findings. It provides a comprehensive explanation 
of the algorithm and presents my research analysis conducted on various optimizers. This paper was submitted to the
CSCSU 2024 Conference, where it was accepted and subsequently published. Additionally, the `Poster.pdf` file serves as a
succinct summary of my Capstone project's work.
