FROM continuumio/anaconda3:5.0.1

ADD . /src
WORKDIR /src

# Installing requirements
RUN conda install --file conda_requirements.txt --yes
RUN pip install -r pip_requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]