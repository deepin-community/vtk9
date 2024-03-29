if (NOT EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/vtk-m/CMakeLists.txt")
  message(FATAL_ERROR
    "VTKm requested, but the VTKm submodule is not initialized. Please run "
    "'git submodule update --init --recursive' in the source directory.")
endif ()

get_property(vtk_smp_backends GLOBAL
  PROPERTY _vtk_smp_backends)

if ("OpenMP" IN_LIST vtk_smp_backends)
  set(VTKm_ENABLE_OPENMP ON)
endif ()

if ("TBB" IN_LIST vtk_smp_backends)
  set(VTKm_ENABLE_TBB ON)
endif ()

set(VTKm_ENABLE_CUDA "${VTK_USE_CUDA}")

set(VTKm_INSTALL_LIB_DIR "${_vtk_build_LIBRARY_DESTINATION}")
set(VTKm_INSTALL_INCLUDE_DIR "${_vtk_build_HEADERS_DESTINATION}/vtkvtkm/vtk-m")
if (DEFINED _vtk_build_LIBRARY_NAME_SUFFIX)
  set(VTKm_CUSTOM_LIBRARY_SUFFIX "-${_vtk_build_LIBRARY_NAME_SUFFIX}")
endif ()
set(VTKm_EXECUTABLE_OUTPUT_PATH "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")
set(VTKm_LIBRARY_OUTPUT_PATH "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")
set(VTKm_BUILD_CMAKE_BASE_DIR "${CMAKE_BINARY_DIR}")
set(VTKm_INSTALL_CONFIG_DIR "${_vtk_build_CMAKE_DESTINATION}/vtkm")
set(VTKm_INSTALL_CMAKE_MODULE_DIR "${VTKm_INSTALL_CONFIG_DIR}/cmake")
# Currently VTK-m only installs its readme and license.
set(VTKm_INSTALL_SHARE_DIR "${_vtk_build_LICENSE_DESTINATION}/vtkvtkm")

if (_vtk_build_INSTALL_HEADERS)
  set(VTKm_INSTALL_ONLY_LIBRARIES OFF)
else ()
  set(VTKm_INSTALL_ONLY_LIBRARIES ON)
endif ()

# Make sure VTK-m is compiled for VTK types.
set(VTKm_USE_DEFAULT_TYPES_FOR_VTK ON)

set(VTKm_USE_DEFAULT_SYMBOL_VISIBILITY OFF)
set(VTKm_ENABLE_RENDERING OFF)
set(VTKm_ENABLE_TESTING OFF)
set(VTKm_ENABLE_BENCHMARKS OFF)
set(VTKm_ENABLE_DOCUMENTATION OFF)
set(VTKm_ENABLE_EXAMPLES OFF)
set(VTKm_ENABLE_CPACK OFF)
set(VTKm_USE_DOUBLE_PRECISION OFF)
set(VTKm_USE_64BIT_IDS "${VTK_USE_64BIT_IDS}")
set(VTKm_NO_ASSERT ON)

set(VTKm_SKIP_LIBRARY_VERSIONS "${VTK_WHEEL_BUILD}")

# VTK-m uses stricter warning checks resulting in more warnings when VTK-m
# is enabled.
# Disable VTK-m warning flags and just rely on VTK's warning flags.
set(VTKm_ENABLE_DEVELOPER_FLAGS OFF)

if(VTKm_ENABLE_CUDA)
  set(BUILD_SHARED_LIBS OFF)
endif()

add_subdirectory(vtk-m)
vtkm_setup_job_pool()

vtk_module_add_module(VTK::vtkm
  HEADER_ONLY)
vtk_module_link(VTK::vtkm INTERFACE vtkm_cont vtkm_filter)
