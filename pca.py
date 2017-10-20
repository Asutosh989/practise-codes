import numpy

def pca_function(data,k):
    number_cols = len(data[0])   
    number_rows = len(data)    
    mean_of_matrix = []
    for index_cols in range(0,number_cols):    
        sumi = 0
        for index_rows in range(0,number_rows):
            sumi = sumi + data[index_rows][index_cols]
        mean_of_matrix.append(sumi/number_rows)
    

    for index_cols in range(0,number_cols):
        for index_rows in range(0,number_rows):
            data[index_rows][index_cols] = data[index_rows][index_cols] - mean_of_matrix[index_cols]
    #Correcto        
    cov = covariances(data);     
    eigen = eigenvectors(cov);    
    eigen = sorted(eigen, key=lambda x: x[0])  
    for index_ei in range(0,len(eigen)):
        eigen[index_ei] = eigen[index_ei][1]

    return eigen[:k]

def covariances(data):
    return numpy.cov(data)

def eigenvectors(cov):
    eigen_vv = []
    eigenvectors = numpy.linalg.eig(cov)[1]
    eigenvalues = numpy.linalg.eig(cov)[0]
    for num_eigenvalues in range(0,len(eigenvalues)):
        eigen_vv.append((eigenvalues[num_eigenvalues],list(eigenvectors[num_eigenvalues])))
    return eigen_vv

    
print(pca_function([[1,2,3],[2,3,4],[3,4,5],[5,6,7]],2))
