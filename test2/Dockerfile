FROM python:3.10 as builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.10-bullseye
WORKDIR /code
COPY --from=builder /root/.local /root/.local
RUN apt update
RUN apt install lame -y

ENV PATH=/root/.local:$PATH
CMD ["python", "-u", "main.py"]
