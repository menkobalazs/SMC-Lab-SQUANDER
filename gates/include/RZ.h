/*
Created on Fri Jun 26 14:13:26 2020
Copyright 2020 Peter Rakyta, Ph.D.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

@author: Peter Rakyta, Ph.D.
*/
/*! \file RZ.h
    \brief Header file for a class representing a rotation gate around the Z axis.
*/

#ifndef RZ_H
#define RZ_H

#include "U3.h"
#include "matrix.h"
#include "matrix_real.h"
#define _USE_MATH_DEFINES
#include <math.h>


/**
@brief A class representing a RZ gate.  The matrix of the gate is [exp(i*varphi/2),0;0,exp(i*varphi/2) ]. The input rotation angle is varphi/2.
*/
class RZ: public U3 {


public:

/**
@brief NullaRZ constructor of the class.
*/
RZ();


/**
@brief Constructor of the class.
@param qbit_num_in The number of qubits spanning the gate.
@param target_qbit_in The 0<=ID<qbit_num of the target qubit.
@param theta_in logical value indicating whether the matrix creation takes an argument theta.
@param phi_in logical value indicating whether the matrix creation takes an argument phi
@param lambda_in logical value indicating whether the matrix creation takes an argument lambda
*/
RZ(int qbit_num_in, int target_qbit_in);

/**
@brief Destructor of the class
*/
~RZ();


/**
@brief Call to apply the gate on the input array/matrix by U3*input
@param parameters An array of parameters to calculate the matrix of the U3 gate.
@param input The input array on which the gate is applied
*/
void apply_to( Matrix_real& parameters, Matrix& input );


/**
@brief Call to apply the gate on the input array/matrix by input*U3
@param parameters An array of parameters to calculate the matrix of the U3 gate.
@param input The input array on which the gate is applied
*/
void apply_from_right( Matrix_real& parameters, Matrix& input );

/**
@brief ???????????????
*/
virtual std::vector<Matrix> apply_derivate_to( Matrix_real& parameters, Matrix& input );

/**
@brief Call to set the final optimized parameters of the gate.
@param Phi Real parameter standing for the parameter phi.
*/
void set_optimized_parameters( double Phi );

/**
@brief Call to get the final optimized parameters of the gate.
@param parameters_in Preallocated pointer to store the parameters Theta, Phi and Lambda of the U3 gate.
*/
Matrix_real get_optimized_parameters();

/**
@brief Calculate the matrix of a U3 gate gate corresponding to the given parameters acting on a single qbit space.
@param Theta Real parameter standing for the parameter theta.
@param Phi Real parameter standing for the parameter phi.
@param Lambda Real parameter standing for the parameter lambda.
@return Returns with the matrix of the one-qubit matrix.
*/
void parameters_for_calc_one_qubit( double& ThetaOver2, double& Phi, double& Lambda);

/**
@brief Call to create a clone of the present class
@return Return with a pointer pointing to the cloned object
*/
RZ* clone();

/**
@brief Calculate the matrix of a U3 gate gate corresponding to the given parameters acting on a single qbit space.
@param PhiOver2 Real parameter standing for the parameter phi/2.
@return Returns with the matrix of the one-qubit matrix.
*/
Matrix calc_one_qubit_u3(double PhiOver2 );


};


#endif //U3

