class Personal:
    def __init__(self, name, address, phone, postal_code, country, region):
        self.name = name
        self.address = address
        self.phone = phone
        self.postal_code = postal_code
        self.country = country
        self.region = region


class Information:
    def __init__(self, cuisines, categories, has_menu):
        self.cuisines = cuisines
        self.categories = categories
        self.has_menu = has_menu

class Sites:
    def __init__(self, website_url, resource_uri):
        self.website_url = website_url
        self.resource_uri = resource_uri