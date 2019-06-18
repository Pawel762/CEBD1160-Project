FROM ubuntu:latest


#running update & installing Python3 with the required Libraries.
 
RUN apt-get update 
RUN apt-get -y install python3 
RUN apt -y install python3-pip 
RUN pip3 install numpy seaborn scipy sklearn

#Create Grahps directory
ADD . /chart/

#including the python3 script and the data to process.

COPY Pawe_Kaluski_Final_Project_CEBD1160_wine.py .
COPY wine.data .

#Command to run the script.

CMD ["python3","-u","Pawe_Kaluski_Final_Project_CEBD1160_wine.py"]
