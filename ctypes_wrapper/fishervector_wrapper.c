#include "generic-driver.h"
#include <vl/generic.h>
#include <vl/fisher.h>

#define VL_SIFT_DRIVER_VERSION 0.1
#define VL_F_TYPE VL_TYPE_FLOAT


void _vl_fisher(int dimension,
		int numClusters,
		void * means,
		void * covariances,
		void * priors,
		int numDataToEncode,
		void * dataToEncode, //data, etc.. are float array pointers
		void * encoding){

    
    // run fisher encoding
    vl_fisher_encode
      (encoding, VL_F_TYPE,
       (float *) means, dimension, numClusters,
       (float *) covariances,
       (float *) priors,
       (float *) dataToEncode, numDataToEncode,
       VL_FISHER_FLAG_IMPROVED
       );

}


