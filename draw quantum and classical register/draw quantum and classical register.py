import qiskit
from qiskit import *


qr = QuantumRegister(2) #build two qubit quantum register
cr = ClassicalRegister(2) #need measurement so imprt the classical register
qc = QuantumCircuit(qr, cr) 
qc.draw(output='mpl')

 
