#include "generic-driver.h"
#include <vl/generic.h>
#include <vl/gmm.h>

#define VL_SIFT_DRIVER_VERSION 0.1


void _vl_gmm(int dimension,
	     int numData,
	     int numClusters,
	     int max_iterations,
	     void * data, //data, etc.. are float array pointers
	     void * means, //means of gaussians
	     void * covariances, //diagonal of covariance matrix
	     void * priors // weights of gaussians
	     ){

  VlGMM * gmm;
  gmm = vl_gmm_new(VL_TYPE_FLOAT, dimension, numClusters);
  vl_gmm_set_max_num_iterations (gmm, max_iterations) ;
  vl_gmm_set_initialization (gmm,VlGMMRand);
  vl_gmm_cluster(gmm, data, numData);
  
  float * means_op = (float *) means;
  float * cov_op = (float *) covariances;
  float * priors_op = (float *) priors;
  float * means_g = (float *) vl_gmm_get_means(gmm);
  float * covariances_g = (float *) vl_gmm_get_covariances(gmm);
  float * priors_g = (float *) vl_gmm_get_priors(gmm);

  for(int i=0; i<numClusters; i++){
    for(int j=0; j<dimension; j++){
      *(means_op+i*dimension+j) = *(means_g+i*dimension+j);
      *(cov_op+i*dimension+j) = *(covariances_g+i*dimension+j);
    }
    *(priors_op+i) = *(priors_g+i);
  }
  
  vl_gmm_delete(gmm);
}
