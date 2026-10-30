# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RYGate(1.4989100685639651), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.reset(qc.qubits)
qc.append(RYGate(1.4989100685639651), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_788733 = QuantumRegister(2, name='qr_788733')
qc.add_register(qr_788733)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit_aer import AerSimulator
simulator = AerSimulator()
qc = transpile(qc, backend=simulator, basis_gates=None, optimization_level=1, coupling_map=None)
counts = simulator.run(qc, shots=346).result().get_counts(qc)
RESULT = counts
print(counts)
