FROM python:3

ADD MainScores.py /

ADD scores.txt /

ADD requierments.txt /

ADD templates /templates

RUN pip3 install -r requierments.txt

CMD [ "python", "./MainScores.py" ]

