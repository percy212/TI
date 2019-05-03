# -TI
truncated_svd

 행렬 a(mxn)와 자연수 t를 입력받고, t가 a의 n보다 클 경우 오류메시지를 출력하고 0 세 개를 반환한다.
 a <= n일 때는 행렬 a를 numpy.linalg.svd() 라이브러리 함수를 이용해서 svd를 한 다음
 입력 받은 t에 맞게 u와 s, vt를 수정한 trunc_u, trunc_d, trunc_vt를 반환하는 함수.
 
pca

 행렬 a(mxn)와 자연수 t를 입력받고, t가 a의 n보다 클 경우 오류메시지를 출력하고 0 을 반환한다.
 행렬 a에서 평균을 빼서 a_cen 행렬을 만든 다음 numpy.linalg.svd를 이용해서 vt를 얻는다.
 이는 a의 공분산 행렬의 eigenvector 행렬이 된다. -> Cov(X,Y) = E((X-μ)(Y-υ))
 이 vt를 입력받은 t에 맞게 수정해서 pcv를 리턴한다.


numpy.linalg.svd는 eigenvalue를 내림차순으로 정렬하기 때문에 이 라이브러리 함수를 이용하면
제일 많은 정보를 담고 있는 t개의 벡터를 쉽게 얻을 수 있다.
