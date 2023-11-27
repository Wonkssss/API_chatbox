FROM python:3
WORKDIR /projects
ADD requirements.txt .
ADD . .
RUN pip3 install uvicorn 
RUN pip install fastapi

#ENTRYPOINT ["uvicorn", "chatroom_project.main:app", "--host", "0.0.0.0", "--port", "5501"]
ENTRYPOINT ["uvicorn", "chatroom_project.main:app", "--host", "127.0.0.1", "--port", "5502"]


