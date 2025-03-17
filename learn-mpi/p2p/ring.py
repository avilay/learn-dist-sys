import os

from cprint import cprint
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank != 0:
    # prime all other process to recv the token
    token = comm.recv(source=rank - 1, tag=0)
    cprint(rank, f"[{os.getpid()}:{rank}] Received token {token} from {rank-1}")
else:
    # rank 0 is the one that generates the token
    token = -1

# every process including rank-0 forwards the token to the next one
# e.g., for 3 processes of rank 0, 1, 2, rank-2 will
# will forward the token to rank-(2+1 % 3), i.e., rank-0
# but rank-0 is not ready to recv yet
dest_rank = (rank + 1) % comm.size
comm.send(token, dest=dest_rank, tag=0)

# now that rank-0 has generated and forwarded the token it is
# ready to recv.
if rank == 0:
    token = comm.recv(source=comm.size - 1, tag=0)
    cprint(rank, f"[{os.getpid()}:{rank}] Received token {token} from {comm.size-1}")
