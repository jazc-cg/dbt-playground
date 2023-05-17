FROM python:latest

WORKDIR /app

RUN echo "installing requirements....."
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org \
    -U pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org \
    --no-cache sqlalchemy==1.4.46 psycopg2==2.8.6 psycopg2-binary==2.8.6
RUN echo ""

COPY app.py app.py
CMD ["python", "-u", "app.py"]
