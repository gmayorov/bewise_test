FROM python:3.10 as builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.10-bullseye
WORKDIR /code
COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local;/root/.local/bin:$PATH
CMD ["python", "-u", "main.py"]
