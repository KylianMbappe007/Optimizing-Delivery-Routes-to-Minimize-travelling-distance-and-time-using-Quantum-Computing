print("typical bell test with hadamard input")
import qiskit
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.draw(output='mpl')

print("identifying the pauli matrix")
print("typical bell test with hadamard input")
import qiskit
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.draw(output='mpl')

print("identifying the pauli matrix")
from qiskit.quantum_info import Pauli

ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')

observer = [ZZ, ZI, IZ, XI, IX, XX]
print([qc] * len(observer), observer)

print("identify the estimated time taken")
from qiskit_aer.primitives import Estimator

estimator = Estimator()
job = estimator.run([qc] * len(observer), observer)
print(job.result())

print("when does it output either qubit 1 or qubit 0")
import matplotlib.pyplot as plt
data_observers = ['ZZ', 'ZI', 'IZ', 'XX', 'XI', 'IX']
values = job.result().values
plt.plot(data_observers, values)
plt.show()
