from model.user_model import *
from model.vacations_model import *
from facade.travel_facade import *
travel_facade = TravelFacade()
# user_to_like = UserModel(1, None, None, None, None, None)
# vacation_to_like = VacationsModel(10, None, None, None, None, None, None)


class Test:
    def __init__(self):
        self.facade = TravelFacade()
        
       
    
    user_to_like = UserModel(1, None, None, None, None, None)
    vacation_to_like = VacationsModel(10, None, None, None, None, None, None)
    u1 = UserModel(None, "shukyy", "shukk", "shukyk@shuk.il", "77777", 2)
    v1 = VacationsModel(None, 2, "cars week", "2025-10-20", "2025-10-27", 9000, "sport car")
    l_u1 = UserModel(None, None, None, "udi@israeli.il", "ui12345", None)
    u_v1 = VacationsModel(14, 2, "sport cars week", "2025-10-20", "2025-10-27", 9000, "sport car")
    d_v = VacationsModel(14, None, None, None, None, None, None)

        # ------------adding user------------------
   
    def add_user(self):
        new_user_info = False

        try:
            new_user_info = travel_facade.new_user(self.u1)

        except ValueError as err:
            print("Error: ", err)
        except TypeError as err:
            print("Error: ", err)
        except Exception as err:
            print("Error: ", err)
        finally:
            if new_user_info:
                print(new_user_info)
                print("\n welcome new user")
            else:
                print("the function is not ok")

        print("\n finish❤")

         #---------------adding vacation-----------------
    
    def add_vacation(self):
        vacation_added = False

        try:
            vacation_added = travel_facade.add_vacation(self.v1)

        except ValueError as err:
            print("Error: ", err)
        except TypeError as err:
            print("Error: ", err)
        except Exception as err:
            print("Error: ", err)
        finally:
            if vacation_added:
                print(vacation_added)
                print("\n The value was added")
            else:
                print("the function is not ok")

            print("Finish❤")

        # -------------view all vacations----------------
    
    def view_all_vacations(self):
        all_vac = False

        try:
            all_vac = travel_facade.display_all_vacations()

        except Exception as err:
            print("Error: ", err)
        finally:
            if all_vac:
                print(all_vac)
                print("\n have a nice vacation")
            else:
                print("the function is not ok")

            print("finish❤")

        ## ------------------user login--------------------------------
    
    def user_login(self):
        user_info = False

        try:
            user_info = travel_facade.user_login(self.l_u1)
        except ValueError as err:
            print("Error: ", err)
        except Exception as err:
            print("Error: ", err)
        finally:
            if user_info:
                print(user_info)
                print("welcome back")
            else:
                print("the function is not ok")

            print("\n finish❤")

        # ------------------vacation update------------------
    
    def update_vacation(self):
        latest_vac = False

        try:
            latest_vac = travel_facade.change_vacation_facade(self.u_v1)
        except ValueError as err:
            print("Error: ", err)
        except TypeError as err:
            print("Error: ", err)
        except Exception as err:
            print("Error: ", err)
        finally:
            if latest_vac:
                print(latest_vac)
                print("\n vacation updated")
            else:
                print("the function is not ok")

            print("finish❤")

        # -----------------deleting vacation--------------------
    
    def delete_vacation(self):
        delet_vac = False

        try:
            delet_vac = travel_facade.eraes_vacation(self.d_v)
        except TypeError as err:
            print("Error: ", err)
        except Exception as err:
            print("Error: ", err)
        finally:
            if delet_vac:
                print("the vacation on ", delet_vac, " is deleted")
            else:
                print("the function is not ok")

            print("finish❤")

        # -------------------adding like-------------------------
    
    def add_like(self):


        del_like = False

        try:
            del_like = travel_facade.insert_like(self.user_to_like, self.vacation_to_like)

        except Exception as err:
            print("Error : ", err)

        finally:
            
            if del_like is not None:
                print(f"user_id: {self.user_to_like.user_id}, vacation_id: {self.vacation_to_like.vacation_id}")
                print (" the like added successfully")
            else:
                print("The function is not ok")

            print("Finish❤")

        # ------------------deleting like--------------
    
    def delete_like(self):
        del_like = False

        try:
            del_like = travel_facade.eraes_like(self.user_to_like, self.vacation_to_like)

        except Exception as err:
            print("Error : ", err)

        finally:
            if del_like:
                print(f"user_id: {self.user_to_like.user_id}, vacation_id: {self.vacation_to_like.vacation_id}")
                print("the row is deleted")
            else:
                print("the function is not ok")

            print("Finish❤")

        # ------------------function to run all-------------------
    
    def test_all(self):
        # self.add_user()
        # self.add_vacation()
        # self.view_all_vacations()
        # self.user_login()
        # self.update_vacation()
        # self.delete_vacation()
        # self.add_like()
        self.delete_like()


test = Test()

   