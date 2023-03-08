
from fastapi import FastAPI
import pandas as pd
import os
import json 
df = pd.read_csv('top-1m.csv', index_col=1, squeeze = True, header=None)
d = dict(df.to_dict())

app = FastAPI()

sourceage = int(os.path.getmtime('/opt/fastapi-siterank/top-1m.csv'))




@app.get("/domain/{domain}")
async def siteRank(domain):
    try: 
        return {"domain":domain,"rank": f'{d[domain]:,}', "sourceLastUpdated":sourceage }
    except:

        return {"rank": "> 1,000,000","domain":domain, "sourceLastUpdated":sourceage}

@app.get("/top100")
async def top100():
    try: 
        return {"results":df[1:101].to_json(orient='columns') }
    except:
        return {"results" : "error"}

#print(df[1:100])
