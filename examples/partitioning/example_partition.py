from squander.partitioning.partition import (
    get_qubits,
    qasm_to_partitioned_circuit
)


def example_partition():
    filename = "examples/partitioning/qasm_samples/heisenberg-16-20.qasm"
    
    max_partition_size = 4
    partitined_circuit, parameters = qasm_to_partitioned_circuit( filename, max_partition_size )

    print("Partitions (#id: num_gates {qubits}):")
    total = 0
    for i, partition in enumerate(top_c.get_Gates()):
        num_gates = len(partition.get_Gates())
        qubits = set.union(*(get_qubits(gate) for gate in partition.get_Gates()))
        total += num_gates
        print(f"#{i + 1}: {num_gates} {qubits}")
    print(f"Total gates: {total}")
    
    
    


if __name__ == "__main__":
    example_partition()
