"""
mpiexec -n 4 python -m p2p.recv_status
"""

import os
from cprint import cprint
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def log(msg):
    if isinstance(msg, MPI.Status):
        status = msg
        cprint(
            rank,
            f"[{os.getpid()}:{rank}] Recv status: {status.count} bytes tagged with {status.tag} from rank {status.source}",
        )
    else:
        cprint(rank, f"[{os.getpid()}:{rank}] {msg}")


def main():
    if rank != 0:
        data = {"a": 7, "b": 3.14}
        log("Sending data")
        comm.send(data, dest=0, tag=10 + rank)
    else:
        while True:
            try:
                status = MPI.Status()  # This is an out param
                data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
                log(f"Recvd data {data}")
                log(status)
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()
