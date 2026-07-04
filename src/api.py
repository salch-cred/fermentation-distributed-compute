from fastapi import FastAPI
from pydantic import BaseModel
from src.fermentation_compute import YeastNode

app = FastAPI(title="Fermentation Distributed Compute API")
node = YeastNode()

class SubstrateRequest(BaseModel):
    substrate_amount: float

@app.post("/ferment")
def ferment(req: SubstrateRequest):
    work = node.feed_substrate(req.substrate_amount)
    return {
        "work_done": float(work),
        "ethanol_concentration": float(node.ethanol_concentration)
    }
