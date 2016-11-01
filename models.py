class Personal:
    def __init__(self, nameNum, name, address, country, region):
        self.nameNum = nameNum
        self.name = name
        self.address = address
        self.country = country
        self.region = region


class Information:
    def __init__(self, cuisinesNum, cuisines, categories, has_menu):
        self.cuisinesNum = cuisinesNum
        self.cuisines = cuisines
        self.categories = categories
        self.has_menu = has_menu


class Sites:
    def __init__(self, website_url, resource_uri):
        self.website_url = website_url
        self.resource_uri = resource_uri