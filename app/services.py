import hashlib
from sqlalchemy.orm import Session
from app.models import URL

def generate_short_code(long_url: str) -> str:
    return hashlib.md5(long_url.encode()).hexdigest()[:6]

def shorten_url(db: Session, long_url: str):
    existing_url = db.query(URL).filter(URL.long_url == long_url).first()
    if existing_url:
        return existing_url

    short_code = generate_short_code(long_url)
    new_url = URL(long_url=long_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

def get_long_url(db: Session, short_code: str):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    if url:
        url.visit_count += 1
        db.commit()
        db.refresh(url)
    return url
