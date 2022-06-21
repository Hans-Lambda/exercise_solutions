from pydantic import BaseModel
from datetime import datetime


# Pydantic will generate constructor, function to transform object to JSON
# only provide attributes with type annotation
# CTRL + Leftclick - open associated file

class Bike(BaseModel):

    id_: str
    name: str
    manufacturer: str
    # datetime.strptime(datetime, "%d/%m/%y")
    year: datetime
