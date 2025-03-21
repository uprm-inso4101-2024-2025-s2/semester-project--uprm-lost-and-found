from sqlalchemy.orm import Session
from database.models import FoundItems
from datetime import datetime, timedelta

def search_found_items(db: Session, name=None, category=None, location=None, date=None, recent_hours=None):
    """Search found items based on multiple filters."""
    query = db.query(FoundItems)

    # Apply filters
    if name:
        query = query.filter(FoundItems.f_description.ilike(f"%{name}%"))
    
    if category:
        query = query.filter(FoundItems.f_additionaldetails.ilike(f"%{category}%"))  # Adjust if needed
    
    if location:
        query = query.filter(FoundItems.f_placefound.ilike(f"%{location}%"))  # Adjust
    
    if date:
        query = query.filter(FoundItems.f_publishdate == date)
    
    if recent_hours:
        cutoff = datetime.now() - timedelta(hours=recent_hours)
        query = query.filter(FoundItems.f_publishdate >= cutoff.date())
    
    query = query.order_by(FoundItems.f_publishdate.desc())

    return query.all()
