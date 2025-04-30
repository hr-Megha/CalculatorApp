class Phone:
    def set_color(self,color):
         self.color=color

    def set_cost(self,cost):
         self.cost=cost

    def show_color(self):
         return self.color

    def show_cost(self):
         return self.cost

    def make_call(self):
        print("Making phone call")

    def play_game(self):
            print("playing game")


p1=Phone()  # object creation


p1.make_call() # calling the function
p1.play_game()

p1.set_color("blue") #setting the value
p1.set_cost(999)

p1.show_color()
p1.show_cost()