from .database import SessionLocal
from .models import Glasses


class DataAccess:

    def __init__(self):
        self.db = SessionLocal()

    def get_all_glasses(self):
        return self.db.query(Glasses).all()

    def search_glasses(self, keyword):
        return (
            self.db.query(Glasses)
            .filter(
                Glasses.glasses_name.ilike(f"%{keyword}%")
                | Glasses.brand_name.ilike(f"%{keyword}%")
            )
            .all()
        )

    def filter_by_price(self, min, max):
        return self.db.query(Glasses).filter(Glasses.price.between(min, max)).all()

    def import_glasses(self, items):
        try:
            for item in items:
                existing = (
                    self.db.query(Glasses).filter_by(glasses_id=item.glasses_id).first()
                )
                if existing:
                    existing.link = item.link
                    existing.glasses_name = item.glasses_name
                    existing.brand_name = item.brand_name
                    existing.price = item.price
                    existing.img_url = item.img_url
                else:
                    new_item = Glasses(
                        glasses_id=item.glasses_id,
                        link=item.link,
                        glasses_name=item.glasses_name,
                        brand_name=item.brand_name,
                        price=item.price,
                        img_url=item.img_url,
                    )
                    self.db.add(new_item)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error importing glasses: {e}")
            return False
