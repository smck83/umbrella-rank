FROM debian:stable
LABEL maintainer="s@mck.la"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ntp python3 pip wget unzip \
    && mkdir -p /opt/fastapi-siterank/
# download Top 1 million cisco Umbrella sites
ADD top-1m.csv main.py run.py /opt/fastapi-siterank/
RUN wget http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip -P /opt/fastapi-siterank/ && unzip -o /opt/fastapi-siterank/top-1m.csv.zip -d /opt/fastapi-siterank/
RUN pip3 install fastapi pandas uvicorn["standard"]
WORKDIR /opt/fastapi-siterank


VOLUME ["/opt/fastapi-siterank/"]

ENTRYPOINT /usr/bin/python3 -u /opt/fastapi-siterank/run.py

EXPOSE 8000/tcp
