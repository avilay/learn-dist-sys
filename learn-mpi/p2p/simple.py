"""
$ mpiexec -n 2 python -m p2p.simple
"""
import os
from dataclasses import dataclass

import numpy as np
from cprint import cprint
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


@dataclass
class Cookie:
    flavor: str
    calories: int

    def __repr__(self) -> str:
        return f"<Cookie(flavor={self.flavor}, calories={self.calories})>"


if rank == 0:
    data = {"a": 7, "b": 3.14}
    cprint(rank, f"[{os.getpid()}:{rank}] Sending data")
    comm.send(data, dest=1, tag=11)

    cookies = [Cookie("Chocoloate Chip", 200), Cookie("Oatmeal Raisin", 180)]
    cprint(rank, f"[{os.getpid()}:{rank}] Sending cookies")
    comm.send(cookies, dest=1, tag=12)

    rng = np.random.default_rng()
    array = rng.standard_normal(10, dtype=np.float32)
    cprint(rank, f"[{os.getpid()}:{rank}] Sending ndarray")
    comm.send(array, dest=1, tag=13)
# elif rank == 1:
else:
    data = comm.recv(source=0, tag=11)
    cprint(rank, f"[{os.getpid()}:{rank}] Recvd data {data}")

    cookies = comm.recv(source=0, tag=12)
    cprint(rank, f"[{os.getpid()}:{rank}] Recvd cookies {cookies}")

    array = comm.recv(source=0, tag=13)
    cprint(rank, f"[{os.getpid()}:{rank}] Recvd ndarray {array}")
