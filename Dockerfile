# Docker file that installs docker container for Selprom
#
# build with: "sudo docker build -t selprom ."

# Install basic image
FROM continuumio/anaconda3:5.2.0

# Install additional tools
RUN conda create -n py36 python=3.6 anaconda
RUN conda activate py36
RUN conda install -c conda-forge flask-restful=0.3.6
RUN pip install msgpack
RUN pip install pysbol

# Start the server
ENTRYPOINT ["python"] 
CMD ["/appoptdes/doeServe.py"]

# Open server port
EXPOSE 8989
