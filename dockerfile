FROM python:3.8

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["python", "run_microservice.py"]
CMD ["python", "threeApp/run.py"]
