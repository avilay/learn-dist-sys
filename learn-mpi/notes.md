# MPI

MPI stands for Message Passing Interface. This is a specification and there are several implementations like MPICH, OpenMPI, etc. These implement the MPI specs in a shared library with C APIs. `mpi4py` is a Python wrapper on top of the MPI APIs. According to its documentation it works with any MPI implementation. Came across this interesting looking [HPC course](https://www.hpc-training.org/xsede/moodle/) on Moodle that uses MPI.

## Installation Instructions
For most purposes, don't try to install some impelementation of MPI and then try to `pip install mpi4py`. Use Miniconda and conda-forge. It will install everything in the venv, including a working version of MPI, not sure which. I'll just need to install a package called `gxx_linux-64`.

I have created a bunch of AMIs to easily setup an MPI cluster.

  * `ubuntu-base-dev`: This is just the standard Ubuntu 22.04 LTS image with updated, upgraded, and `build-essential` pkgs installed.
  * `mpi-base`: This is built on top of `ubuntu-base-dev` with Miniconda and `mpi4py` installed in a venv called `hpc`.
  * `mpi-head-base`: This is just `mpi-base` but with an ssh keypair created and the right ssh config created.
  * `mpi-worker-base`: This is just `mpi-base` but with the public key of the `mpi-base-head` image added to its `~/.ssh/authorized_keys` file to set up keyless ssh from head.

```
$ sudo apt update
$ sudo apt upgrade
$ reboot  # for some reason Ubuntu20 compalins after upgrade
$ sudo apt install build-essential
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod 700 Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda3-latest-Linux-x86_64.sh
$ exit
SSH reconnect
$ conda --version
conda 4.12.0
$ conda create --name hpc numpy
$ conda activate hpc
$ conda install gxx_linux-64
$ conda install -c conda-forge mpi4py
$ mpiexec -n 5 python -m mpi4py.bench helloworld
```

Enable password less SSH from head to all the workers. No need to set it up for worker to worker or worker to head.

1. Generate an SSH keypair on the head
```
$ ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa
```

2. Set up ssh config on the head
Edit `.ssh/config` and add the following entries:

```
Host *
    ForwardAgent yes
Host *
    StrictHostKeyChecking no
```

3. Copy the newly created `id_rsa.pub` from the head node to all the worker nodes.

4. SSH into all the workers from head.

Test distributed MPI
1. On the head node, create a hostfile with IP addresses of all the workers, that will be used by mpiexec. Lets call it `mpi-hosts.txt`. It should look like -
```
172.31.31.26
172.31.31.103
```

2. Rub the `helloworld` test program.
```
(hpc) ubuntu@ip-172-31-18-199:~$ mpiexec -n 6 --hostfile mpi-hosts.txt python -m mpi4py.bench helloworld
Hello, World! I am process 0 of 6 on ip-172-31-31-26.
Hello, World! I am process 1 of 6 on ip-172-31-31-103.
Hello, World! I am process 2 of 6 on ip-172-31-31-26.
Hello, World! I am process 3 of 6 on ip-172-31-31-103.
Hello, World! I am process 4 of 6 on ip-172-31-31-26.
Hello, World! I am process 5 of 6 on ip-172-31-31-103.
```

Notice, that the head does not execute anything! It is just used to launch the workers.

### Other Installation Methods 
There are other ways to create and run MPI clusters in AWS using one of Elastic Fiber Adapter, AWS ParallelCluster, and AWS Batch. There is also an MIT project called the StarCluster toolkit that can be used for set up.

  * Using Elastic Fiber Adapater has the pretty good instructions [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html).
  * [Here](https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-configuring.html) are the instructions for setting up AWS ParallelCluster and then [here](https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorials_03_batch_mpi.html) are the instructions for using it along with AWS Batch.
  * [Here](https://mpitutorial.com/tutorials/launching-an-amazon-ec2-mpi-cluster/) are the instructions on using StarCluster toolkit.



This is the `helloworld` implementation 

```python
#!/usr/bin/env python
"""
Parallel Hello World
"""

from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

sys.stdout.write(
    "Hello, World! I am process %d of %d on %s.\n"
    % (rank, size, name))
```

## API

* `send`
* `recv`
* `sendrecv`
* `isend`
* `irecv`
* Barrier sync
* `bcast`
* `scatter`
* `gather`
* `allgather`
* `alltoall`
* `reduce`
* `reduce_scatter`
* `allreduce`





```
MPI_Send(
    void* data,
    int count,
    MPI_Datatype datatype,
    int destination,
    int tag,
    MPI_Comm communicator)
    
MPI_Recv(
    void* data,
    int count,
    MPI_Datatype datatype,
    int source,
    int tag,
    MPI_Comm communicator,
    MPI_Status* status)
    
MPI_Probe(
		int source,
		int tag,
		MPI_Comm comm,
		MPI_Status* status
)

MPI_Get_count(
		MPI_Status* status,
		MPI_Datatype datatype,
		int* count
)
```

