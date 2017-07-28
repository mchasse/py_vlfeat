import numpy
import ctypes
import os

NB="""
this wrapper calls functions from the vlfeat library
so vlfeat's bin needs to be in LD_LIBRARY_PATH
"""

dirpath = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.cdll.LoadLibrary(os.path.join(dirpath,'vlfeat_wrapper.so'))

def get_dsift_num_patches(rows, cols, step, bin_size):
        return lib.get_dsift_num_patches(cols, rows, step, bin_size)

def dsift(im, step, bin_size):
        """
        returns the dsift descriptor for an image in a 1xn numpy matrix
        """
        im = numpy.array(im)
        rows, cols = im.shape
        desc_size = 128*lib.get_dsift_num_patches(cols, rows, step, bin_size)
        descriptor = numpy.zeros((1,desc_size), dtype=numpy.float32)
        im = im.astype(numpy.float32)
        lib._dsift(ctypes.c_void_p(im.ctypes.data),
                   ctypes.c_void_p(descriptor.ctypes.data),
                   ctypes.c_int(rows),
                   ctypes.c_int(cols),
                   ctypes.c_int(step),
                   ctypes.c_int(bin_size))
        return descriptor


def gmm(num_clusters, data_matrix, max_iterations=100):
        """
        returns the gmm means and covariances from vl feat
        """
        data_matrix = numpy.matrix(data_matrix)
        num_data, dimension = data_matrix.shape
        data_matrix = data_matrix.astype(numpy.float32)
        means = numpy.zeros((num_clusters,dimension), dtype=numpy.float32)
        covariances = numpy.zeros((num_clusters,dimension), dtype=numpy.float32)
        priors = numpy.zeros((num_clusters,1), dtype=numpy.float32)
        lib._vl_gmm(ctypes.c_int(dimension),
                    ctypes.c_int(num_data),
                    ctypes.c_int(num_clusters),
                    ctypes.c_int(max_iterations),
                    ctypes.c_void_p(data_matrix.ctypes.data),
                    ctypes.c_void_p(means.ctypes.data),
                    ctypes.c_void_p(covariances.ctypes.data),
                    ctypes.c_void_p(priors.ctypes.data))
        
        return means, covariances, priors

def fisher(means, covariances, priors, data_matrix):
        """
        returns the fisher vector representation for the data rows
        using the provided gmm model parameters
        """
        means = numpy.array(means)
        covariances = numpy.array(covariances)
        priors = numpy.array(priors)
        data_matrix = numpy.array(data_matrix)
        assert numpy.alltrue(means.shape == covariances.shape), "inconsistent dimensions"
        assert means.shape[0] == len(priors), "inconsistent dimensions"
        num_data, dimension = data_matrix.shape
        data_matrix = data_matrix.astype(numpy.float32)
        means = means.astype(numpy.float32)
        covariances = covariances.astype(numpy.float32)
        priors = priors.astype(numpy.float32)
        num_clusters = len(priors)
        encoding = numpy.zeros((num_clusters, 2*dimension), dtype=numpy.float32)
        lib._vl_fisher(ctypes.c_int(dimension),
		       ctypes.c_int(num_clusters),
                       ctypes.c_void_p(means.ctypes.data),
                       ctypes.c_void_p(covariances.ctypes.data),
                       ctypes.c_void_p(priors.ctypes.data),
                       ctypes.c_int(num_data),
                       ctypes.c_void_p(data_matrix.ctypes.data),
                       ctypes.c_void_p(encoding.ctypes.data))
        
        return encoding
