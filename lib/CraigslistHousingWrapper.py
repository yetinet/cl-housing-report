from logging import WARN
from craigslist import CraigslistHousing

# WrapperClass
class CraigslistHousingWrapper(CraigslistHousing):

    def __init__(self, site="sfbay", area="scz", category="apa", filters={"max_bedrooms":1000, "max_bathrooms":1000, "max_ft2":99999}, log_level=WARN):
        super().__init__(site=site, area=area, category=category, filters=filters, log_level=log_level)
