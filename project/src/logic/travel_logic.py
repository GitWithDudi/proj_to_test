from utils.dal import *
from model.user_model import *
from model.vacations_model import *
import re


class TravelLogic:

    def __init__(self,):
        self.dal = DAL()


    def add_user_logic(self, user):
        sql = """
        insert into users(f_name, 
        l_name, 
        email, 
        password_num, 
        role_id) 
        values (%s,%s,%s,%s,%s)
        """
        insert_row = self.dal.insert_dal(sql,(user.f_name, 
            user.l_name, 
            user.email, 
            user.password_num, 
            user.role_id,))
        return insert_row
 

    
    def one_user_logic(self, user):
        sql = """
        select * from travel_db.users 
        where users.email = %s and users.password_num = %s
        """
        lonly_user = self.dal.get_one(sql,(user.email, user.password_num,))
        return lonly_user
    

        
    def email_exist_logic(self, email):
       
        sql = """
            select users.email from travel_db.users
            where users.email = %s
            """
        result= self.dal.get_one(sql,(email,))
        if result:
            return True
        return False
    
    

    def all_vacations_logic(self):
    
        sql = """
            select * from travel_db.vacations
            order by start_date ASC
        """ 
        result =self.dal.get_table(sql)
        return result



    def add_new_vacation_logic(self,vac):
        
        sql = """
        insert into travel_db.vacations
            (country_id, discreption, 
            start_date, 
            end_date, 
            price, 
            impeg_name)
        values (%s, %s, %s, %s, %s, %s)
        """
        new_vac = self.dal.insert_dal(sql, (vac.country_id, 
            vac.discreption, 
            vac.start_date, 
            vac.end_date, 
            vac.price, 
            vac.impeg_name,))
        return new_vac





    def update_vacation_logic(self,vac):
        
        sql = """
            update travel_db.vacations 
            set country_id = %s,
                discreption = %s,
                start_date = %s,
                end_date = %s, 
                price = %s, 
                impeg_name = %s 
            where vacation_id = %s
            """
        latest_vac = self.dal.update_dal(sql, (vac.country_id, 
            vac.discreption, 
            vac.start_date, 
            vac.end_date, 
            vac.price, 
            vac.impeg_name, 
            vac.vacation_id,))
        return latest_vac





    def delete_vacation_logic(self, vac):
        sql = """
            delete from travel_db.vacations
            where vacation_id = %s
            """
        del_vac = self.dal.delete_dal(sql,(vac.vacation_id,))
        return del_vac
    

    def add_like(self, user, vac):

            sql = """
                insert into travel_db.likes(user_id,vacation_id)
                values (%s, %s)
                """
            answer = self.dal.insert_dal(sql,(user.user_id, vac.vacation_id,))
            return answer
  



    def delete_like(self, user, vac):

        sql = """
            delete from travel_db.likes
            where user_id = %s and vacation_id = %s
            """
        answer = self.dal.delete_dal(sql,(user.user_id, vac.vacation_id,))
        return answer

            
    # this function make suring syntax email is legal 
            
    def legal_email(self, email):
        email_syntax = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' 
        if re.match(email_syntax, email):
            return True
        return False   
    
    
  