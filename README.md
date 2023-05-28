# miapi
a python api server，reply query from xiao ai speakers

## 问题
1. ERROR: Could not install packages due to an OSError: Missing dependencies for SOCKS support.
 - pip不支持socks5代理，需要先安装 pysocks
 - conda pysocks
2. 生成依赖
 - 安装pipreqss
 - pipreqs . --encoding=utf8 --force
3. docker
    ```sh
    conda create -n miapi python=3.10
    conda activate miapi

    conda install pysocks
    pip install pipreqs

    pip install -r requirements.txt numpy -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

    pipreqs . --encoding=utf8 --force

    docker build --tag miapi .
    docker tag miapi:latest miapi:v1.0.0

    docker rmi python-docker:v1.0.0
    
    docker run -d -p 8000:5000 --name miapi miapi:v1.0.0

    docker stop miapi
    docker restart miapi
    docker rm miapi
    ```

4. 测试请求
```
 curl -k --insecure "https://api.tinypig.top:8443"
```