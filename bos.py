# bos

payoffs_w = [4,2]
payoffs_m = [2,4]

def eval_results(w_choice, m_choice):
    if w_choice == "opera" and m_choice == "opera":
        return (4,2)
    elif w_choice == "football" and m_choice == "football":
        return (2,4)
    else:
        return (0,0)