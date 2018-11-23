class Person:

    country = 'cn'
    @classmethod
    def set_country(cls,new_country):
        cls.country = new_country

    @staticmethod
    def set_static_country(new_country):
        Person.country = new_country


Person.setStaticCountry('eu')

