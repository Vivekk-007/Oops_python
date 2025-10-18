class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""  
        self.logged_in = False
        self.menu()


    def menu(self):
        user_input = input("""welcome to chatbook please select an option:
                           1.press 1 to signup
                           2.press 2 to login
                           3.press 3 to write a post
                           4.press 4 to message a friend
                           5.press 5 to view profile
                           6.press 6 to logout
                           7.press any other key to exit to exit""") 
         
        if user_input == '1':
            pass
        elif user_input == '2':     
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        elif user_input == '5':
            pass        
        elif user_input == '6':
            pass    
        else:
            exit()            

app = chatbook()    