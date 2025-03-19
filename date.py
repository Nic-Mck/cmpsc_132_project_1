class Date() :
    def __init__(self, month:str, day:str, year:str) -> None :
        self.__month = month
        self.__day = day
        self.__year = year

    def display(self) -> None : 
        print(f'{self.__month}/{self.__day}/{self.__year}')

    def __str__(self) -> str :
        return f'{self.__month}/{self.__day}/{self.__year}'
    
    # Getters / Setters

    def get_month(self) -> str : 
        return self.__month
    
    def get_day(self) -> str : 
        return self.__day
    
    def get_year(self) -> str : 
        return self.__year
    
    def set_month(self, new_month:str) -> str : 
        self.__month = new_month
    
    def set_day(self, new_day:str) -> str : 
        self.__day = new_day
    
    def set_year(self, new_year:str) -> str : 
        self.__year = new_year
