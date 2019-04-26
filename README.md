# -TI
truncatedSVD

 행렬 A(mxn)와 자연수 t를 입력받고, t가 A의 n보다 클 경우 오류메시지를 출력하고 0 세 개를 반환한다.
 A <= n일 때는 행렬 A를 numpy.linalg.svd() 라이브러리 함수를 이용해서 svd를 한 다음
 입력 받은 t에 맞게 U와 D, V를 수정한 trunc_U, trunc_D, trunc_V를 반환하는 함수.
 
PCA

 행렬 A(mxn)와 자연수 t를 입력받고, t가 A의 n보다 클 경우 오류메시지를 출력하고 0 을 반환한다.
 행렬 A에서 평균을 빼서 A_cen 행렬을 만든 다음 numpy.linalg.svd를 이용해서 V를 얻는다.
 이는 A의 공분산 행렬의 eigenvector 행렬이 된다. -> Cov(X,Y) = E((X-μ)(Y-υ))
 이 V를 입력받은 t에 맞게 수정해서 PCV를 리턴한다.


numpy.linalg.svd는 eigenvalue를 내림차순으로 정렬하기 때문에 이 라이브러리 함수를 이용하면
제일 많은 정보를 담고 있는 t개의 벡터를 쉽게 얻을 수 있다.
