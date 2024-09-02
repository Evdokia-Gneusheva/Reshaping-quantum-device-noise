import boto3
from braket.circuits import Circuit, Noise, Gate, Instruction, ResultType
from braket.aws import AwsDevice
from braket.devices import LocalSimulator

from matplotlib import pyplot as plt
import numpy as np
import scipy
import string
import networkx as nx

pi = np.pi

phi = pi/9
theta = 0
theta0 = 0.01 * pi # 0.328 * pi | 0.647 * pi | 0.965 * pi
n_shots = 10000


# phi = pi
# theta = pi/2
# theta0 = 0.772 * pi
# n_shots = 1


# s3 = boto3.resource('s3')
# print('Available s3 buckets:')
# for bucket in s3.buckets.all():
#     print(bucket.name)
    

# s3 = boto3.resource(
#     's3',
#     aws_access_key_id='AKIAW3MECVAESKHRN4OK',
#     aws_secret_access_key='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'
# )
# print('Available S3 buckets:')
# for bucket in s3.buckets.all():
#     print(bucket.name)


# b_runOnDevice = True
# garnet = "arn:aws:braket:eu-north-1::device/qpu/iqm/Garnet"
# aws_device = AwsDevice(garnet)
 
# device = LocalSimulator(backend="braket_dm")
    
############################# TO CHECK EQUIVALENCE ############################

# q01234XerrorU = Circuit().rx(0, phi)\
#                           .rz(0, theta)\
#                           .cnot(0,1)\
#                           .cnot(0,2)\
#                           .ry(0, theta0)\
#                           .cnot(0,3)\
#                           .cnot(1,3)\
#                           .cnot(1,4)\
#                           .cnot(2,4)\
            
          
# print(q01234XerrorU)
# result = device.run(q01234XerrorU, shots = n_shots).result()
# counts = result.measurement_counts

# # Calculate measurement counts for each qubit
# qubit_counts = {i: {'0': 0, '1': 0} for i in range(6)}

# for bitstring, count in counts.items():
#     for qubit, bit in enumerate(bitstring):
#         qubit_counts[qubit][bit] += count

# print("Measurement counts for the first circuit:")
# for qubit in range(6):
#     print(f"Qubit {qubit}: 0 -> {qubit_counts[qubit]['0']}, 1 -> {qubit_counts[qubit]['1']}")


# circuit = Circuit().prx(4, 0.5 * pi, 1.5 * pi)\
#                     .prx(2, 0.5 * pi, 1.5 * pi)\
#                     .prx(1, 0.5 * pi, 1.5 * pi)\
#                     .prx(0, 0.111111111111111 * pi, 0)\
#                     .prx(5, 0.5 * pi, 1.5 * pi)\
#                     .cz(0, 1)\
#                     .cz(0, 2)\
#                     .prx(1, 0.5 * pi, 0.5 * pi)\
#                     .prx(2, 0.5 * pi, 0.5 * pi)\
#                     .prx(0, 0.01 * pi, 0.5 * pi)\
#                     .cz(0, 5)\
#                     .cz(3, 5)\
#                     .prx(3, 0.5 * pi, 1.5 * pi)\
#                     .prx(5, 0.5 * pi, 0.5 * pi)\
#                     .cz(5, 3)\
#                     .prx(3, 0.5 * pi, 0.5 * pi)\
#                     .prx(5, 0.5 * pi, 1.5 * pi)\
#                     .cz(3, 5)\
#                     .prx(3, 0.5 * pi, 1.5 * pi)\
#                     .prx(5, 0.5 * pi, 0.5 * pi)\
#                     .cz(1, 3)\
#                     .cz(1, 4)\
#                     .prx(3, 0.5 * pi, 0.5 * pi)\
#                     .cz(2, 4)\
#                     .prx(4, 0.5 * pi, 0.5 * pi)\
# print(circuit)

# result2 = device.run(circuit, shots = n_shots).result()
# counts2 = result2.measurement_counts


# # Calculate measurement counts for each qubit in the second circuit
# qubit_counts2 = {i: {'0': 0, '1': 0} for i in range(15)} 

# for bitstring, count in counts2.items():
#     for qubit, bit in enumerate(bitstring):
#         qubit_counts2[qubit][bit] += count

# print("Measurement counts for the second circuit:")
# for qubit in range(15):  
#     print(f"Qubit {qubit}: 0 -> {qubit_counts2[qubit]['0']}, 1 -> {qubit_counts2[qubit]['1']}")
    
    
############################# TO RUN ON IQM GARNET ############################

# circuit = Circuit().prx(3, 0.5 * pi, 1.5 * pi)\
#                     .prx(4, 0.5 * pi, 1.5 * pi)\
#                     .prx(8, 0.5 * pi, 1.5 * pi)\
#                     .prx(9, 0.111111111111111 * pi, 0)\
#                     .prx(14, 0.5 * pi, 1.5 * pi)\
#                     .cz(9, 8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                         .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                             .cz(9,8)\
#                     .cz(9, 4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                         .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                             .cz(9,4)\
#                     .prx(8, 0.5 * pi, 0.5 * pi)\
#                     .prx(4, 0.5 * pi, 0.5 * pi)\
#                     .prx(9, 0.965 * pi, 0.5 * pi)\
#                     .cz(9, 14)\
#                     .cz(13, 14)\
#                     .prx(13, 0.5 * pi, 1.5 * pi)\
#                     .prx(14, 0.5 * pi, 0.5 * pi)\
#                     .cz(14, 13)\
#                     .prx(13, 0.5 * pi, 0.5 * pi)\
#                     .prx(14, 0.5 * pi, 1.5 * pi)\
#                     .cz(13, 14)\
#                     .prx(13, 0.5 * pi, 1.5 * pi)\
#                     .prx(14, 0.5 * pi, 0.5 * pi)\
#                     .cz(8, 13)\
#                     .cz(8, 3)\
#                     .prx(13, 0.5 * pi, 0.5 * pi)\
#                     .cz(4, 3)\
#                     .prx(3, 0.5 * pi, 0.5 * pi)\
#                     # .measure(9)\
#                     # .measure(8)\
#                     # .measure(4)\
#                     # .measure(13)\
#                     # .measure(3)\
#                     # .measure(14)
# # .measure(13) <-> .measure(4)     

# circuit = Circuit().add_verbatim_box(circuit)

# if b_runOnDevice:
#     awsTask = aws_device.run(circuit, shots = n_shots)


