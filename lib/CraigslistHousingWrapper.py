from logging import WARN
from craigslist import CraigslistHousing

# WrapperClass
class CraigslistHousingWrapper(CraigslistHousing):

    def __init__(self, site="sfbay", area="scz", category="apa", filters=None, log_level=WARN):
        super().__init__(site=site, area=area, category=category, filters=filters, log_level=log_level)
