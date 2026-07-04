# Fermentation Distributed Compute

A decentralized load balancing and consensus protocol modeled on the fermentation chemistry of yeast colony dynamics.

Nodes act as yeast cells consuming "substrates" (tasks/jobs) and producing "metabolites" (token completions). High concentration of localized computed metabolites regulates regional activity to prevent computational thermal runaways.

## Usage
```bash
python examples/run_fermentation_sim.py
```


## FastAPI API Service
The project includes a FastAPI server wrapper. 

### Running the API
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```
- **Interactive docs**: Navigate to `/docs` for swagger documentation.
- **POST `/ferment`**: Consumes substrates to perform load-balanced calculations.
