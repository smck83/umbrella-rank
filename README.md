# Cisco Umbrella Rank FastAPI

This Docker container is running FastAPI and downloads the top 1,000,000 domains from Cisco(which is updated daily) on build.

You can run the container using
`docker run -it -p 8000:8000  smck83/umbrella-rank`

http://localhost:8000/domain/github.com returns

`{"domain":"github.com","rank":"2,508"}`
