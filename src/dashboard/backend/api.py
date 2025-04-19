# src/dashboard/backend/api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
DATABASE_URL = "sqlite:///./metrics.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Metric model for the database
class MetricModel(Base):
    __tablename__ = "metrics"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class Metric(BaseModel):
    name: str
    value: float

@app.post("/metrics/", response_model=Metric)
def add_metric(metric: Metric):
    db: Session = SessionLocal()
    db_metric = MetricModel(name=metric.name, value=metric.value)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    db.close()
    return db_metric

@app.get("/metrics/", response_model=List[Metric])
def get_metrics(skip: int = 0, limit: int = 10, sort_by: Optional[str] = None):
    db: Session = SessionLocal()
    query = db.query(MetricModel)

    if sort_by:
        if sort_by == "name":
            query = query.order_by(MetricModel.name)
        elif sort_by == "value":
            query = query.order_by(MetricModel.value)

    metrics = query.offset(skip).limit(limit).all()
    db.close()
    return metrics

@app.get("/metrics/aggregate/", response_model=dict)
def aggregate_metrics():
    db: Session = SessionLocal()
    metrics = db.query(MetricModel).all()
    db.close()

    if not metrics:
        raise HTTPException(status_code=404, detail="No metrics found")

    values = [metric.value for metric in metrics]
    return {
        "average": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }

# Example usage
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
