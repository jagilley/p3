# bos
import random

class mab:
    def __init__(self, gender):
        self.gender = gender
        self.choice1_rewards = 0
        self.choice2_rewards = 0
    
    def pick_something(self):
        if self.choice1_rewards == self.choice2_rewards:
            return random.choice(["opera", "football"])
        elif self.choice1_rewards > self.choice2_rewards:
            return "opera"
        else:
            return "football"
    
    def note_rewards(self, my_choice, my_reward):
        if my_choice == "opera":
            self.choice1_rewards += my_reward
        else:
            self.choice2_rewards += my_reward

    def __repr__(self):
        return f"I am a {self.gender}. My c1_rew is {self.choice1_rewards} and my c2_rew is {self.choice2_rewards}"

def eval_results(w_choice, m_choice):
    if w_choice == "opera" and m_choice == "opera":
        print("opera it is")
        return (4,2)
    elif w_choice == "football" and m_choice == "football":
        print("football it is")
        return (2,4)
    else:
        print("we do nothing")
        return (0,0)

if __name__=="__main__":
    print("--------NEW SIM-------------")
    man = mab("man")
    woman = mab("woman")
    for epoch in range(30):
        m_choice = man.pick_something()
        w_choice = woman.pick_something()
        print("woman chooses", w_choice, "and man chooses", m_choice)
        results = eval_results(m_choice, w_choice)
        man.note_rewards(m_choice, results[1])
        woman.note_rewards(w_choice, results[0])
        print(man)
        print(woman)