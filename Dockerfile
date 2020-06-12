FROM mail4sreeni/oraconnect

WORKDIR /myapp

ADD hi.py /myapp

CMD exec python3.6 hi.py
