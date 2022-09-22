Description: Fix mpi4py search
Author: Anton Gladky <gladk@debian.org>
Last-Update: 2021-09-17

--- vtk9-9.0.3+dfsg1.orig/Parallel/MPI4Py/vtk.module
+++ vtk9-9.0.3+dfsg1/Parallel/MPI4Py/vtk.module
@@ -12,4 +12,3 @@ DEPENDS
 PRIVATE_DEPENDS
   VTK::ParallelMPI
   VTK::mpi
-  VTK::mpi4py
