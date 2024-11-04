from logic.travel_logic import *
from utils.dal import *
from datetime import datetime

current_date = datetime.now()  # this row giving current date any time

class TravelFacade:
    def __init__(self):
        self.logic = TravelLogic()
        self.dal = DAL()


    def new_user(self,user):
        if  not user.f_name or not user.l_name  or not user.email or not user.password_num or not user.role_id:
            raise ValueError ("all fields cannot be empty")
        elif not self.logic.legal_email(user.email):
            raise ValueError ("the email syntax is not legal")
        elif type(user.role_id) is not int:

            raise TypeError ("role id must be an integer")
        elif len(user.password_num) < 4:

            raise ValueError ("password must be 4 digits or more")
        elif  self.logic.email_exist_logic(user.email):

            raise ValueError ("the email address already exists")
        elif user.role_id == 1:

            raise ValueError("admin user can adding only in database manager")

        
        result = self.logic.add_user_logic(user)
        return result


    

    def user_login(self, e_p):
        if not e_p.email or not e_p.password_num:
            raise ValueError("All fields must be filled in")
        if not self.logic.legal_email(e_p.email):
            raise ValueError ("the email syntax is not legal")
        if not self.logic.email_exist_logic(e_p.email):
            raise ValueError("Email does not exist un system")
        if len(e_p.password_num) < 4:
            raise ValueError ("password must be 4 digits or more")
        
        key = self.logic.one_user_logic(e_p)

        if key is None:
            raise ValueError("the passwod is not correct")
        
        return key
    
    
    
    def display_all_vacations(self):
        result = self.logic.all_vacations_logic()
        return result
    

    def add_vacation(self,vac):
        if  not vac.country_id or not vac.discreption  or not vac.start_date or not vac.end_date or not vac.price or not vac.impeg_name:
            raise ValueError ("all fields cannot be empty")
        if type(vac.country_id) is not int:
            raise TypeError ("country_id must be an integer")
        if type(vac.price) is not int:
            raise TypeError ("price must be an integer")
        if vac.price > 10000:
            raise ValueError ("price cannot be more 10000")
        if vac.price <= 0:
            raise ValueError ("price cannot be negative")
        start_date = datetime.strptime(vac.start_date, '%Y-%m-%d')  # this row translate the string date to object date
        end_date = datetime.strptime(vac.end_date, '%Y-%m-%d')   # this row translate the string date to object date
        if end_date <= start_date:
            raise ValueError ("end_date must be after start_date")
        if start_date < current_date:
            raise ValueError ("start_date must be after current_date")
        
        result = self.logic.add_new_vacation_logic(vac)
        return result
    
    
    def change_vacation_facade(self, vac):
        if not vac.country_id or not vac.discreption or not vac.start_date or not vac.end_date or not vac.price:
            raise ValueError ("all fields cannot be empty")
        if type(vac.country_id) is not int:
            raise TypeError ("country_id must be an integer")
        if type(vac.price) is not int:
            raise TypeError ("price must be an integer")
        if vac.price > 10000:
            raise ValueError ("price cannot be more 10000")
        if vac.price <= 0:
            raise ValueError ("price cannot be negative")
        start_date = datetime.strptime(vac.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(vac.end_date, '%Y-%m-%d')
        if end_date <= start_date:
            raise ValueError ("end_date must be after start_date")
        
        latest = self.logic.update_vacation_logic(vac)
        return latest
    

    def eraes_vacation(self,vac_id):
        if type(vac_id.vacation_id) is not int:
            raise TypeError("vacation_id must be integer")
        commit = self.logic.delete_vacation_logic(vac_id)
        return commit


    
    def eraes_like(self, vac, user):
        result = self.logic.delete_like(vac, user)
        return result
    


    def insert_like(self, vac, user):
        result = self.logic.add_like(vac, user)
        return result