
from fastapi import FastAPI
import pandas as pd
df = pd.read_csv('top-1m.csv', index_col=1, squeeze = True)
d = dict(df.to_dict())

app = FastAPI()





@app.get("/domain/{domain}")
async def siteRank(domain):
    try: 
        return {"domain":domain,"rank": f'{d[domain]:,}'}
    except:

        return {"rank": "> 1,000,000","domain":domain}

