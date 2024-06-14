#---------------------------BAND CLASS START---------------------------
class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []

    # BAND--------NAME
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        self._name = value

    # BAND--------HOMETOWN
    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if hasattr(self, '_hometown'):
            raise AttributeError("Hometown cannot be changed once set")
        if not isinstance(value, str):
            raise TypeError("Hometown must be a string")
        if len(value) == 0:
            raise ValueError("Hometown must be greater than 0 character")
        self._hometown = value

    # BAND---------CONCERTS()
    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    # BAND---------------VENUES
    def venues(self):
        unique_venues = set(concert.venue for concert in self.concerts())
        return list(unique_venues)

    # BAND------Band play_in_venue(venue, date)
    def play_in_venue(self, venue, date):
        new_concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(new_concert)
        return new_concert

    # BAND----------Band all_introductions()
    def all_introductions(self):
        intros = []
        for concert in self.concerts():
            intro = f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            intros.append(intro)
        return intros


#---------------------------BAND CLASS END---------------------------


#---------------------------CONCERT CLASS START---------------------------
class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    # CONCERT---------DATE
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if len(date) == 0:
            raise ValueError("Date must be greater than 0 character")
        self._date = date

    # CONCERT---------BAND
    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        if not isinstance(band, Band):
            raise TypeError("Band must be an instance of Band")
        self._band = band

    # CONCERT----------VENUE
    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        if not isinstance(venue, Venue):
            raise TypeError("Venue must be an instance of Venue")
        self._venue = venue

    # CONCERT--------Concert hometown_show()
    def hometown_show(self):
        return self.band.hometown == self.venue.city

    # CONCERT----------Concert introduction()
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
#---------------------------CONCERT CLASS END---------------------------


#---------------------------VENUE CLASS START---------------------------
class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    # VENUE-----------NAME
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be greater than 0 character")
        self._name = name

    # VENUE------------CITY
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        if len(city) == 0:
            raise ValueError("City must be greater than 0 character")
        self._city = city

    # VENUE---------CONCERTS()
    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    # VENUE---------BANDS()
    def bands(self):
        unique_bands = set(concert.band for concert in self.concerts())
        return list(unique_bands)
#---------------------------VENUE CLASS END---------------------------
