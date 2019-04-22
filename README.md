# -TI
truncatedSVD

 행렬 A를 numpy.linalg.svd() 라이브러리 함수를 이용해서 svd를 한 다음 입력 받은 t에 맞게 U와 D, V를 수정한
 trunc_U, trunc_D, trunc_V를 반환하는 함수.
 
PCA

 행렬 A에서 평균을 빼서 A_cen 행렬을 만든 다음 numpy.linalg.svd를 이용해서 V를 얻는다.
 이는 A의 공분산 행렬의 eigenvector 행렬이 된다. -> Cov(X,Y) = E((X-μ)(Y-υ))
 이 V를 입력받은 t에 맞게 수정해서 PCV를 리턴한다.
