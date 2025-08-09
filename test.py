# import QuantumCircuit from qiskit library
# import Aer from qiskit_aer library
from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer

# Bring QuantumCircuit and put it inside "Elia" virable for use
# Bring Hadamard To Make 1 & 0 (At the same time and moment) Happend [That's the Goal of Quantum Computers]
# Make The 0, 1, 2, 3, 4, 5 on (if the light 0 is on) or off
# Measure All The QuantumCircuit  
Elia = QuantumCircuit(6, 6)
Elia.h(0)
Elia.cx(0, 5)
Elia.measure_all()  

# We Need an 'Aer' Simulator (Not a Real Quantum Computer). Bring qasm_simulator
# We Need an 'execute' so we can Bring 'Elia' and 'Simulator' both. The measure in shots = 1300
# We Need "Job" so we can get counts inside the result
Simulator = Aer.get_backend('qasm_simulator')
result = execute(Elia, Simulator, shots=1300).result()
counts = result.get_counts()

# Importing matplotlib.pyplot as plt
# We brings the keys and values (get_counts)
# We are showing the results on Bar Chart
from matplotlib import pyplot as plt
plt.bar( counts.keys(), counts.values() )
plt.show()

# Show the raw quantum measurement results (counts) in the console using Bar Chart
print(counts)

