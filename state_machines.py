class MealyState:
    def __init__(self, name):           # """ table of the state must be represented by the dictionary in the following order:
        self.state_table = {}           # { 'input1': ['output', 'next_state_name'],
        self.name = name                #   'input2': ['output', 'next_state_name'],
                                        #   'input3': ['output', 'next_state_name'], ... } """

    def add_to_table(self, input_, output_, next_state_):
        truth_table = [output_, next_state_]
        self.state_table[input_] = truth_table

class MealyMachine:
    def __init__(self, name):
        self.name = name
        self.current_state = ""
        self.states = []    #it storages MealyState objects

    def add_state(self, state_obj):
        self.states.append(state_obj)

    def next_clock(self, input_):
        for state in self.states:
            if state.name == self.current_state:
                self.current_state = state.state_table[input_][1]
                return state.state_table[input_][0]

    def machine_init(self):
        self.current_state = self.states[0].name
        while(True):
            var = input("input: ")
            output = self.next_clock(int(var))
            print("output: ", output)



class MooreState:
    def __init__(self, name, value):    # """ table of the state must be represented by the dictionary in the following order:
        self.state_table = {}           # { 'input1': 'next_state_name',
        self.name = name                #   'input2': 'next_state_name',
        self.value = value              #   'input3': 'next_state_name', ... } """

    def add_to_table(self, input_, next_state_):
        self.state_table[input_] = next_state_

class MooreMachine:
    def __init__(self, name):
        self.name = name
        self.current_state = ""
        self.states = []  # it storages MealyState objects

    def add_state(self, state_obj):
        self.states.append(state_obj)

    def next_clock(self, input_):
        for state in self.states:
            if state.name == self.current_state:
                self.current_state = state.state_table[input_]
                for state2 in self.states:
                    if state2.name == self.current_state:
                        return state2.value


    def machine_init(self):
        self.current_state = self.states[0].name
        while(True):
            var = input("input: ")
            output = self.next_clock(int(var))
            print("output: ", output)



MEALY = 0
MOORE = 1

#Sequency detector 011 on mealy or moore machine -> first choose witch one:
CHOICE = MOORE


if CHOICE == MEALY:
    mealy = MealyMachine("Sequency detecotr")
    MealyState1 = MealyState("A")
    MealyState1.add_to_table(0,0,"B")
    MealyState1.add_to_table(1,0,"A")
    mealy.add_state(MealyState1)

    MealyState2 = MealyState("B")
    MealyState2.add_to_table(0,0,"B")
    MealyState2.add_to_table(1,0,"C")
    mealy.add_state(MealyState2)

    MealyState3 = MealyState("C")
    MealyState3.add_to_table(0,0,"B")
    MealyState3.add_to_table(1,1,"C")
    mealy.add_state(MealyState3)

    mealy.machine_init()

elif CHOICE == MOORE:
    Moore = MooreMachine("Sequency detecotr")
    MooreState1 = MooreState("A", 0)
    MooreState1.add_to_table(0,"B")
    MooreState1.add_to_table(1,"A")
    Moore.add_state(MooreState1)

    MooreState2 = MooreState("B", 0)
    MooreState2.add_to_table(0,"B")
    MooreState2.add_to_table(1,"C")
    Moore.add_state(MooreState2)

    MooreState3 = MooreState("C", 0)
    MooreState3.add_to_table(0,"B")
    MooreState3.add_to_table(1,"D")
    Moore.add_state(MooreState3)

    MooreState3 = MooreState("D", 1)
    MooreState3.add_to_table(0,"B")
    MooreState3.add_to_table(1,"A")
    Moore.add_state(MooreState3)

    Moore.machine_init()