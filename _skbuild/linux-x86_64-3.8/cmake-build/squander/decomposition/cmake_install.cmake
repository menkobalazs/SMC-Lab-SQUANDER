# Install script for directory: /home/menko/squander/sequential-quantum-gate-decomposer/squander/decomposition

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/menko/squander/sequential-quantum-gate-decomposer/_skbuild/linux-x86_64-3.8/cmake-install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so"
         RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/squander/decomposition" TYPE MODULE FILES "/home/menko/squander/sequential-quantum-gate-decomposer/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so"
         OLD_RPATH "/home/menko/squander/sequential-quantum-gate-decomposer/squander:/home/menko/.conda/envs/qgd/lib:"
         NEW_RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_Wrapper.cpython-38-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so"
         RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/squander/decomposition" TYPE MODULE FILES "/home/menko/squander/sequential-quantum-gate-decomposer/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so"
         OLD_RPATH "/home/menko/squander/sequential-quantum-gate-decomposer/squander:/home/menko/.conda/envs/qgd/lib:"
         NEW_RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so"
         RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/squander/decomposition" TYPE MODULE FILES "/home/menko/squander/sequential-quantum-gate-decomposer/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so"
         OLD_RPATH "/home/menko/squander/sequential-quantum-gate-decomposer/squander:/home/menko/.conda/envs/qgd/lib:"
         NEW_RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_non_unitary_adaptive_Wrapper.cpython-38-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so"
         RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/squander/decomposition" TYPE MODULE FILES "/home/menko/squander/sequential-quantum-gate-decomposer/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so"
         OLD_RPATH "/home/menko/squander/sequential-quantum-gate-decomposer/squander:/home/menko/.conda/envs/qgd/lib:"
         NEW_RPATH "$ORIGIN/..:/home/menko/.conda/envs/qgd/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/squander/decomposition/qgd_N_Qubit_Decomposition_custom_Wrapper.cpython-38-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/menko/squander/sequential-quantum-gate-decomposer/_skbuild/linux-x86_64-3.8/cmake-build/squander/decomposition/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
