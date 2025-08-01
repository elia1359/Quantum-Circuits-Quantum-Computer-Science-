# import QuantumCircuit from qiskit library
# import Aer from qiskit_aer library
from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer

# Bring QuantumCircuit and put it inside "Elia" virable for use
# Bring Harmade To Make 1 & 0 (At Same time and mommnet) Happend [That's the Goal of Quantum Computers]
# Make The 0, 1, 2, 3, 4, 5 on (if the light 0 is on) or off
# Measure All The QuantumCircuit  
Elia = QuantumCircuit(6)
Elia.h(0)
Elia.cx(0, 5)
Elia.measure_all()

# We Need an 'Aer' Simulator (Not a Real Quantum Computer). Bring qasm_ simulator
# We Need an 'execute' so we can Bring 'Elia' and 'Simulator both The measure in shots = 1300
# We Need "Job" so we so we can get counts inside the result
Simulator = Aer.get_backend('qasm_simulator')
result = execute(Elia, Simulator, shots=1300). result()
counts = result.get_counts()

# Give The Real Result on the Screen by print the "counts" virable
print(counts)

