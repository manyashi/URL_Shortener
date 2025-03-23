from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .services import shorten_url, get_long_url
from .schemas import URLCreate, URLResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shorten", response_model=URLResponse)
def create_short_url(request: URLCreate, db: Session = Depends(get_db)):
    url = shorten_url(db, request.long_url)
    return URLResponse(short_url=f"http://localhost:8000/{url.short_code}", long_url=url.long_url, visit_count=url.visit_count)

@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = get_long_url(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"message": "Redirect", "long_url": url.long_url}
