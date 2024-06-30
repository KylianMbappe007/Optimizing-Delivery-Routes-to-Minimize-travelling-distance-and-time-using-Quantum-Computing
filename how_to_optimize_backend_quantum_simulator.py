import qiskit
from qiskit import Aer, execute, QuantumCircuit
from qiskit.quantum_info import Pauli, Statevector
from qiskit.visualization import plot_histogram
from qiskit.opflow import PauliExpectation, CircuitSampler, StateFn

# Define the quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Draw the circuit
qc.draw(output='mpl')

# Define the observables
observables = [Pauli('ZZ'), Pauli('ZI'), Pauli('IZ'), Pauli('XX'), Pauli('XI'), Pauli('IX')]

# Choose the Aer simulator backend
backend = Aer.get_backend('qasm_simulator')

# Optimize the backend configuration
shots = 1024  # Number of measurement shots
optimization_level = 3  # Optimization level (0 to 3)

# Execute the circuit on the simulator
job = execute(qc, backend, shots=shots, optimization_level=optimization_level)
result = job.result()

# Get the counts and plot the histogram
counts = result.get_counts(qc)
plot_histogram(counts)

# Calculate expectation values for the observables
state = Statevector.from_instruction(qc)
expectation_values = {}
for observable in observables:
    expectation = PauliExpectation().convert(StateFn(observable, is_measurement=True) @ StateFn(state)).eval()
    expectation_values[str(observable)] = expectation

# Print the expectation values
print("Expectation values:")
for observable, value in expectation_values.items():
    print(f"{observable}: {value}")
