from sqlalchemy.orm import Session
from database.models import LostItems
from datetime import datetime, timedelta

def search_lost_items(db: Session, name=None, category=None, location=None, date=None, recent_hours=None):
    """Search lost items based on multiple filters."""
    query = db.query(LostItems)

    # Apply filters
    if name:
        query = query.filter(LostItems.l_description.ilike(f"%{name}%"))
    
    if category:
        query = query.filter(LostItems.l_information.ilike(f"%{category}%"))  # Adjust if necessary
    
    if location:
        query = query.filter(LostItems.l_information.ilike(f"%{location}%"))  # Adjust if stored differently
    
    if date:
        query = query.filter(LostItems.l_publishdate == date)
    
    if recent_hours:
        cutoff = datetime.now() - timedelta(hours=recent_hours)
        query = query.filter(LostItems.l_publishdate >= cutoff.date())
    
    # Order by most recent
    query = query.order_by(LostItems.l_publishdate.desc())

    return query.all()
