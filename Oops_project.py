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
            self.signup()
        elif user_input == '2':
            self.login()            
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
        elif user_input == '5':
            self.view_profile()
        elif user_input == '6':
            self.logout()
        else:
            exit() 

    def signup(self):
        email = input("enter your email id: ")  
        password = input("enter your password: ")
        self.username = email
        self.password = password
        print("signup successful")
        self.menu() 

    def login(self):
        email = input("enter your email id: ")  
        password = input("enter your password: ")
        if email == self.username and password == self.password:
            self.logged_in = True
            print("login successful")
        else:
            print("invalid credentials")
        self.menu()
    def write_post(self):
        if self.logged_in:
            post = input("write your post: ")
            print("post successful")
        else:
            print("please login to write a post")
        self.menu()
    def message_friend(self):
        if self.logged_in:
            friend = input("enter your friend's name: ")
            message = input("enter your message: ")
            print("message sent to", friend)
        else:
            print("please login to message a friend")
        self.menu()
    def view_profile(self):
        if self.logged_in:
            print("username:", self.username)
        else:
            print("please login to view profile")
        self.menu()
    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("logout successful")
        else:
            print("you are not logged in")
        self.menu()

app = chatbook()

app.signup('vivek', 'vivek123')
