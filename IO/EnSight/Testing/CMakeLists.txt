if (VTK_WRAP_PYTHON)
  vtk_module_test_data(
    Data/EnSight/,REGEX:.*
    Data/EnSight/UndefAndPartial/,REGEX:.*
    Data/EnSight/UndefAndPartialAscii/,REGEX:.*
    )

  add_subdirectory(Python)
endif ()
