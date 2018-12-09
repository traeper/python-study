# Conda 패키지 매니저
Package, dependency and environment management.<br>
패키지 매니저를 이용하면 프로그램을 설치하는 컴퓨터의 운영체제와 사양에 상관 없이 개발환경과 호환되는 환경을 구축하여 프로그래밍을 할 수 있다.
여러 패키지 매니저 중 Conda를 선택하였다.

## 빠른 설명
### 콘다 환경에 패키지 설치

```
$ cd python-study/envs/conda
$ conda env create -f python3.6-environment.yml
```


### 콘다 환경에 패키지 업데이트

```
$ cd python-study/envs/conda
$ conda env update -f python3.6-environment.yml
```

## 환경 관리 방법
1. 컴퓨터에 conda 프로그램(Anaconda 또는 miniconda)을 설치한다.
2. 환경설정 파일 경로로 이동한다. 
    ```
    $ cd python-study/envs/conda 
    $ python3.6-environment.yml
    ``` 
3. 필요한 환경을 설정한다.
    ```
    $ cd python-study/envs/conda
    $ vi python3.6-environment.yml
    
    conda의 dependencies: 항목이나 pip: 항목에 필요한 패키지와 버전을 적어준다.
    ```
4. 환경설정 파일을 이용해서 환경을 구축한다.
    ```
    $ conda env create/update -f python3.6-environment.yml
    ``` 
5. 파이썬 프로그램 실행

## link
* miniconda : https://conda.io/miniconda.html
* reference docs : https://conda.io/docs/
