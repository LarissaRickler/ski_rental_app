
import numpy as np
import numpy.random as rand
import tkinter as tk
from tkinter import messagebox

import ski_rental_algos as sr
import utils as u

# # Ski Rental App

def back_pred():
    root.deiconify()
    window.destroy()
    
def back_pick():
    window.deiconify()
    result_window.destroy()

def back_pick_main():
    root.deiconify()
    window.destroy()
    result_window.destroy()




def set_mode(mode):
    global b
    global x
    global y
    global prediction_mode
    
    b = 100 # cost of ski
    x = rand.randint(1, high = 4 * b + 1) # actual number of skiing days
    prediction_mode = mode
    
    #todo:ajust
    if prediction_mode == "good":
        max_eta = rand.randint(0, 10 + 1) # max prediction error
    elif prediction_mode == "medium":
        max_eta = rand.randint(0, 50 + 1) # max prediction error
    elif prediction_mode == "bad":
        max_eta = rand.randint(0, 4 * b +1) # max prediction error
    else:
        max_eta = rand.randint(0, 4 * b + 1) # max prediction error
        
    eta = np.random.normal(loc = 0, scale = max_eta)  # normally in [-max_eta, max_eta]
    # eta = rand.randint(-max_eta, high = max_eta+1, size = num_samples) # uniformly in [-max_eta, max_eta]
    y = x + eta
    y = int(max(1, min(y, 4 * b)))
      
    global window
    window = tk.Toplevel(root)  # create parent window
    root.withdraw()
    window.title("Ski Rental")
    window.geometry()
    
    message_ski_rental = "\nThe price of the ski is " + str(b) + "€.\nYou chose a " + str(prediction_mode) +\
                         " predicter.\nThe predicted number of skiing days is " + str(y) + ".\n"
 

    text_intro = tk.Message(window, text=message_ski_rental, width=400)
    text_intro.pack()
    
    message_guess = "Choose how many days you want to rent, before you will buy the ski:"
    text_guess= tk.Message(window, text=message_guess, width=500)
    text_guess.pack()
    
    global guessed_x
    guess_x = tk.Scale(window, from_=0, to=4*b, length=550, tickinterval=50, orient=tk.HORIZONTAL)
    guess_x.set(0)
    guess_x.pack()
    
    
    next_window = tk.Button(window, text="See results", height= 1, width=10, command=lambda: calc_results(guess_x.get()))
    next_window.pack()
    
    back = tk.Button(window, text="Back to main", height= 1, width=10, command=back_pred)
    back.pack()
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()





def calc_results(guessed_x):
    
    opt = u.array_to_int(sr.opt(b,np.array([x])))

    tradeoff_lambda = 0.5
    
    alg_det_online = u.array_to_int(sr.alg_det_online(b, np.array([x])))

    alg_naive = u.array_to_int(sr.alg_naive(b, np.array([x]), np.array([y])))

    alg_det = u.array_to_int(sr.alg_det(b, np.array([x]),  np.array([y]), tradeoff_lambda))

    alg_rand_online = u.array_to_int(sr.alg_rand_online(b, np.array([x])))

    alg_rand = u.array_to_int(sr.alg_rand(b, np.array([x]),  np.array([y]), tradeoff_lambda))
    
    global result_window
    result_window = tk.Toplevel(root)  # create parent window
    window.withdraw()
    result_window.title("Ski Rental Results")
    result_window.geometry()
    
    
    message_result = "\nPredicted number of days: " + str(y) +\
                     "\nActual days to ski: " + str(x) +\
                     "\nPrediction error: " + str(abs(x-y)) +\
                     "\nYou chose to rent " + str(guessed_x) + " days." +\
                     "\n\nOptimal cost: " + str(opt) +\
                     "\n\nResults of your guess\n" + u.print_result(u.self_guess(guessed_x, x, b),opt) +\
                     "\n\nResults of deterministic online algorithm\n" + u.print_result(alg_det_online,opt) +\
                     "\n\nResults of naive algorithm with ML\n" + u.print_result(alg_naive,opt) +\
                     "\n\nResults of deterministic algorithm with ML\n" +\
                     "Trust in prediction: " + str(tradeoff_lambda) + "\n" +\
                     u.print_result(alg_det,opt) +\
                     "\n\nResults of randomized online algorithm\n" +\
                     u.print_result(alg_rand_online,opt)+\
                     "\n\nResults of randomized algorithm with ML\n" +\
                     "Trust in prediction: " + str(tradeoff_lambda) + "\n" +\
                     u.print_result(alg_rand,opt) +\
                     "\n"
                     
        
        
                    
    text_result= tk.Message(result_window, text=message_result, width=400)
    text_result.pack()
    
    back = tk.Button(result_window, text="Back", height= 1, width=10, command=back_pick)
    back.pack()

    back_to_main = tk.Button(result_window, text="Back to main", height= 1, width=10, command=back_pick_main)
    back_to_main.pack()

    quit_button = tk.Button(result_window, text="Quit", height= 1, width=10, command=on_closing_result)
    quit_button.pack()
    
    
    result_window.protocol("WM_DELETE_WINDOW", on_closing_result)
    result_window.mainloop()




def on_closing_root():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.deiconify()
        window.destroy() 
        root.destroy()
        
def on_closing_result():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.deiconify()
        window.destroy()
        result_window.destroy()
        root.destroy()



def start():
    global root
    root = tk.Tk()  
    root.title("Ski Rental")
    root.geometry()

    message_info =  "\nSuppose that you are interested in taking ski lessons, " +\
                    "and you start wondering about the equipment needed. " +\
                    "You are not sure if you will really like it, so it is not clear whether you should buy skis " +\
                    "or start renting each time you have a lesson.\n\n" +\
                    "Each time you rent skis, you have to pay 1€, while the total cost of buying skis is 100€.\n" +\
                    "So, the question you want to resolve is the following. " +\
                    "What should be the strategy towards renting/buying so that you do not spend too much money " +\
                    "if the total number of times you will go skiing is not yet known?\n\n" +\
                    "Additionally, you can get a prediction on how many days you will ski."
                                    
    text_info = tk.Message(root, text=message_info, width=600)
    text_info.pack()

    message_pred = "How well should the prediction be?"
                                    
    text_pred = tk.Message(root, text=message_pred, width=380)
    text_pred.pack()

    unknown = tk.Button(root, text="unknown", height= 1, width=10, command=lambda: set_mode("unknown"))
    unknown.pack()

    good = tk.Button(root, text="good", height= 1, width=10, command=lambda: set_mode("good"))
    good.pack()

    medium = tk.Button(root, text="medium", height= 1, width=10, command=lambda: set_mode("medium"))
    medium.pack()

    bad = tk.Button(root, text="bad", height= 1, width=10, command=lambda: set_mode("bad"))
    bad.pack()



    root.protocol("WM_DELETE_WINDOW", on_closing_root)
    root.mainloop()


