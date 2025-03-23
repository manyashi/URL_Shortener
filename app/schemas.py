from pydantic import BaseModel

class URLCreate(BaseModel):
    long_url: str

class URLResponse(BaseModel):
    short_url: str
    long_url: str
    visit_count: int
