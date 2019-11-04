FROM icorrea/miniconda:4.7.12.1-alpine3.10

WORKDIR /root

# Instala as dependencias do projeto
RUN pip install grpcio \
    && pip install grpcio.tools \
    && pip install joblib \
    && pip install sklearn

# Limpa tudo que foi executado e remove arquivos usados apenas na instalação
RUN conda clean -tp -y 

EXPOSE 50052


COPY *.py /root/
COPY modeloml1.pickle /root/

CMD ["python", "grpc_server.py"]

