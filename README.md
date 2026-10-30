# MorphQ++ examples

Standalone Qiskit examples for the RENE 2024 artifact transformations. Each script builds and simulates its own circuit, then prints its measurement counts.

## Setup

Requires Python 3.14 or newer and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
```

## Run an example

Run any script directly:

```sh
uv run python examples/initialize_circuit.py
```

Other scripts are in `examples/`: `reset_circuit.py`, `copy_circuit.py`, `add_barrier.py`, `qpy_roundtrip.py`, `qasm_roundtrip.py`, and `transpilation_backend.py`.
