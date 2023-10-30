#!/usr/bin/env python
# coding: utf-8

# <a href="https://qworld.net" target="_blank" align="left"><img src="../qworld/images/header.jpg"  align="left"></a>
# $ \newcommand{\bra}[1]{\langle #1|} $
# $ \newcommand{\ket}[1]{|#1\rangle} $
# $ \newcommand{\braket}[2]{\langle #1|#2\rangle} $
# $ \newcommand{\dot}[2]{ #1 \cdot #2} $
# $ \newcommand{\biginner}[2]{\left\langle #1,#2\right\rangle} $
# $ \newcommand{\mymatrix}[2]{\left( \begin{array}{#1} #2\end{array} \right)} $
# $ \newcommand{\myvector}[1]{\mymatrix{c}{#1}} $
# $ \newcommand{\myrvector}[1]{\mymatrix{r}{#1}} $
# $ \newcommand{\mypar}[1]{\left( #1 \right)} $
# $ \newcommand{\mybigpar}[1]{ \Big( #1 \Big)} $
# $ \newcommand{\sqrttwo}{\frac{1}{\sqrt{2}}} $
# $ \newcommand{\dsqrttwo}{\dfrac{1}{\sqrt{2}}} $
# $ \newcommand{\onehalf}{\frac{1}{2}} $
# $ \newcommand{\donehalf}{\dfrac{1}{2}} $
# $ \newcommand{\hadamard}{ \mymatrix{rr}{ \sqrttwo & \sqrttwo \\ \sqrttwo & -\sqrttwo }} $
# $ \newcommand{\vzero}{\myvector{1\\0}} $
# $ \newcommand{\vone}{\myvector{0\\1}} $
# $ \newcommand{\stateplus}{\myvector{ \sqrttwo \\  \sqrttwo } } $
# $ \newcommand{\stateminus}{ \myrvector{ \sqrttwo \\ -\sqrttwo } } $
# $ \newcommand{\myarray}[2]{ \begin{array}{#1}#2\end{array}} $
# $ \newcommand{\X}{ \mymatrix{cc}{0 & 1 \\ 1 & 0}  } $
# $ \newcommand{\I}{ \mymatrix{rr}{1 & 0 \\ 0 & 1}  } $
# $ \newcommand{\Z}{ \mymatrix{rr}{1 & 0 \\ 0 & -1}  } $
# $ \newcommand{\Htwo}{ \mymatrix{rrrr}{ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} } } $
# $ \newcommand{\CNOT}{ \mymatrix{cccc}{1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0} } $
# $ \newcommand{\norm}[1]{ \left\lVert #1 \right\rVert } $
# $ \newcommand{\pstate}[1]{ \lceil \mspace{-1mu} #1 \mspace{-1.5mu} \rfloor } $
# $ \newcommand{\greenbit}[1] {\mathbf{{\color{green}#1}}} $
# $ \newcommand{\bluebit}[1] {\mathbf{{\color{blue}#1}}} $
# $ \newcommand{\redbit}[1] {\mathbf{{\color{red}#1}}} $
# $ \newcommand{\brownbit}[1] {\mathbf{{\color{brown}#1}}} $
# $ \newcommand{\blackbit}[1] {\mathbf{{\color{black}#1}}} $

# <font style="font-size:28px;" align="left"><b> Qiskit installation and test </b></font>
# <br>
# _prepared by Abuzer Yakaryilmaz_
# <br><br>

# - [Check your system](#check)
# - [Install qiskit](#install)
# - [Tips](#tips)
# - [Execute an example quantum program](#test)
# - [Complete test](#complete)

# <hr id="check">
# 
# ### Check your system
# 
# Check your system, if Qiskit has already been installed:

# In[5]:


import qiskit
versions = qiskit.__qiskit_version__
print("The version of Qiskit is",versions['qiskit'])
print()
print("The version of each component:")
for key in versions:
    print(key,"->",versions[key])


# **You should be able to see the version number of any library that is already installed in your system.**

# <hr id="install">
# 
# ### Install qiskit
# 
# (If you are an experienced user, visit this link: https://qiskit.org/documentation/install.html)
# 
# You can install Qiskit by executing the following cell:

# In[13]:


get_ipython().system('pip install "qiskit[visualization]" --user')


# __*Restart the kernel*__ (check "Kernel" menu) to apply the changes to the current notebook.

# <hr id="tips">
# 
# ### Tips
# 
# _Any terminal/shell command can be executed in the notebook cells by putting an exclamation mark (!) at the beginning of the command._
# 
# _$\rightarrow$ To update Qiskit to the latest version, execute the following command in a code cell_
# 
#     !pip install -U qiskit --user
#     
# _$\rightarrow$ To uninstall Qiskit, execute the following command in a code cell_
# 
#     !pip uninstall qiskit

# In[ ]:


#!pip install -U qiskit --user
#!pip uninstall qiskit


# <hr id="test">
# 
# ### Execute an example quantum program
# 

# 1) Create a quantum circuit

# In[14]:


# import the objects from qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from random import randrange

# create a quantum circuit and its register objects
qreg = QuantumRegister(2) # quantum register with two quantum bits
creg = ClassicalRegister(2) # classical register with two classical bit
circuit = QuantumCircuit(qreg,creg) # quantum circuit composed by a quantum register and a classical register

# apply a Hadamard gate to the first qubit
circuit.h(qreg[0])

# set the second qubit to state |1>
circuit.x(qreg[1])

# apply CNOT(first_qubit,second_qubit)
circuit.cx(qreg[0],qreg[1])

# measure the both qubits
circuit.measure(qreg,creg)

print("The execution of the cell was completed, and the circuit was created :)")


# 2) Draw the circuit
# 
# _Run the cell once more if the figure is not shown_

# In[16]:


# draw circuit 
circuit.draw(output='mpl')

# the output will be a "matplotlib.Figure" object


# 3) Execute the circuit 1024 times in the local simulator and print the observed the outcomes

# In[3]:


## execute the circuit 1024 times
job = execute(circuit,Aer.get_backend('qasm_simulator'),shots=1024)
# get the result
counts = job.result().get_counts(circuit)
print(counts)


# <hr id="complete">
# 
# ### Complete test
# 
# Here we put all methods and objects of Qiskit used througout this tutorial (see [Qiskit: Quick Reference](Q01_Qiskit_Reference.ipynb) for a complete list).
# 
# By running the cell below, you should be able to test whether your Qiskit installation is ready for our tutorial.
# 
# _It was tested with Qiskit 0.37.0 on July 10, 2022._

# In[4]:


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi

# A quantum circuit is composed by a quantum and a classical register in Qiskit
q = QuantumRegister(5,"q") # this quantum register has 5 qubits
c = ClassicalRegister(5,"c") # this classical register has 5 classical bits

qc = QuantumCircuit(q,c) # a quantum circuit with quantum and classical registers q and c

qc.x(q[2]) # apply x-gate to the qubit "q[2]" of the quantum circuit "qc"
qc.z(q[4]) # apply z-gate to the qubit "q[4]" of the quantum circuit "qc"
qc.h(q[1]) # apply h-gate to the qubit "q[1]" of the quantum circuit "qc"

a = pi/7
qc.ry(2*a,q[3]) # apply ry-gate with the specified angle to the qubit "q[3]" of the quantum circuit "qc"

qc.cx(q[1],q[0]) # apply cx-gate to the qubits "q[1]" and "q[0]" of the quantum circuit "qc"

qc.cu(2*a,0,0,0,q[1],q[0]) # apply controlled rotation operator with the specified angle 
                          #  to the qubits "q[1]" and "q[0]" of the quantum circuit "qc"

qc.ccx(q[2],q[1],q[0]) # apply ccx-gate to the qubits "q[2]", "q[1]", and "q[0]" of the quantum circuit "qc"

qc.barrier()

qc.measure(q[0],c[3]) # measure q[0] and write the output on c[3]
qc.measure(q[1],c[1]) # measure q[1] and write the output on c[1]
qc.measure(q[2],c[4]) # measure q[2] and write the output on c[4]
qc.measure(q[3],c[0]) # measure q[3] and write the output on c[0]
qc.measure(q[4],c[2]) # measure q[4] and write the output on c[2]

display(qc.draw())

qc.barrier()

qc.h(q[0]).c_if(c,5)
qc.x(q[0]).c_if(c,3)
qc.z(q[0]).c_if(c,1)

for i in range(5):
    if i % 2 ==0: qc.h(q[i])
    else: qc.x(q[i])
        
b = 3*pi/11
qc.cu(2*b,0,0,0,q[1],q[0])

display(qc.draw(output='mpl',reverse_bits=True))

job = execute(qc,Aer.get_backend('qasm_simulator'),shots=1000)
counts = job.result().get_counts(qc)   
print("measurement outcomes are:",counts)
print()

q = QuantumRegister(2,"q")
c = ClassicalRegister(2,"c")

qc = QuantumCircuit(q,c)

qc.h(q[0])
qc.ry(a,q[0])
qc.x(q[1])
qc.cx(q[0],q[1])

job = execute(qc,Aer.get_backend('unitary_simulator'),shots=1,optimization_level=0)
precision = 3
current_unitary=job.result().get_unitary(qc,precision).data

print("unitary matrix is")
print(current_unitary)
print()

job = execute(qc,Aer.get_backend('statevector_simulator'),optimization_level=0)
precision = 3
current_quantum_state=job.result().get_statevector(qc,precision).data
print("quantum state is")
for val in current_quantum_state:
    print(str(val.real)+"+"+str(val.imag)+"j")

print()
print("All looks fine :-)")

