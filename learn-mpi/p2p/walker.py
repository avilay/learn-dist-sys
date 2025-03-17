"""
https://mpitutorial.com/tutorials/point-to-point-communication-application-random-walk/
"""
import os
from cprint import cprint
from mpi4py import MPI
from dataclasses import dataclass

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
world_size = comm.size


def log(msg):
    if isinstance(msg, MPI.Status):
        status = msg
        cprint(
            rank,
            f"[{os.getpid()}:{rank}] Recv status: {status.count} bytes tagged with {status.tag} from rank {status.source}",
        )
    else:
        cprint(rank, f"[{os.getpid()}:{rank}] {msg}")


@dataclass
class Walker:
    location: int
    n_steps_left: int


def decompose_domain(world_domain_size: int) -> tuple[int, int]:
    # For a domain size of 17 and 3 process
    # rank-0's domain will start from 17//3 * 0 = 0 and its size will be 17//3 = 5
    # rank-1's domain size will also be 5
    # rank-2's domain size will be 5 + 17%3 = 7
    my_domain_size = (world_domain_size // world_size) + (int(rank == world_size - 1) * world_domain_size % world_size)
    start = (world_domain_size // world_size) * rank

    
    

