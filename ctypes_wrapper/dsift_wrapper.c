#include "generic-driver.h"
#include <vl/generic.h>
#include <vl/stringop.h>
#include <vl/pgm.h>
#include <vl/dsift.h>

#define VL_SIFT_DRIVER_VERSION 0.1

int get_dsift_num_patches(int cols, int rows, int step, int bin_size){
  VlDsiftFilter* dsift_filter_p = vl_dsift_new_basic(cols,rows,step,bin_size); 
  int num = vl_dsift_get_keypoint_num(dsift_filter_p);
  vl_dsift_delete(dsift_filter_p);
  return num;
}

void _dsift(const void * data, void * descriptor, int rows, int cols, int step, int bin_size){

  const float * df_ptr = (float *) data;
  float * des_ptr = (float *) descriptor;
  VlDsiftFilter* dsift_filter_p = vl_dsift_new_basic(cols,rows,step,bin_size); 
  vl_dsift_process(dsift_filter_p, df_ptr);

  int number_of_patches = dsift_filter_p->numFrameAlloc;
  for(int i=0; i<number_of_patches; i++){
    for(int j=0; j<128;j++){
      *(des_ptr + i*128+j)= dsift_filter_p->descrs[i*128+j];
    }
  }

  vl_dsift_delete(dsift_filter_p);
}

