# Ski Rental App
### An implementation of several online algorithms for the ski rental problem
<br />


This repository contains an implementation of learning augmented online algorithms for the ski rental problem described in 
[Improving Online Algorithms via ML Predictions](https://papers.nips.cc/paper/2018/file/73a427badebe0e32caa2e1fc7530b7f3-Paper.pdf) [[1]](#1) as well as an implementation of the best known deterministic [[2]](#2) and randomized [[3]](#3) online algorithms. <br /> <br />


Running the main file of the implementation starts a little game. <br />


Suppose that you are interested in taking ski lessons, and you start wondering about the equipment needed. 
You are not sure if you will really like it, so it is not clear whether you should buy skis or start renting each time you have a lesson.
Each time you rent skis, you have to pay 1€, while the total cost of buying skis is 100€. So, the question you want to resolve is the following. What should be the strategy towards renting/buying so that you do not spend too much money if the total number of times you will go skiing is not yet known? <br />
Additionally, you can get a prediction on how many days you will ski. This prediction can be good, but it can also be very bad. <br />

Based on this prediction, choose how many days you will rent the ski before you decide to buy them. <br />

Afterwards, you can compare how well your guess was, compared to the implemented algorithms. <br />

Have fun!



## Get it to work

First clone the repository to your preferred location:

```bash
# HTTPS
git clone https://github.com/LarissaRickler/ski_rental_app.git

# SSH
git clone git@github.com:LarissaRickler/ski_rental_app.git
```

I recommend creating a separate environment before installing the dependencies, e. g. via 

```bash
conda create -n ski_rental_app
conda activate ski_rental_app
```

We then need to install the dependencies. The code depends on (assuming python3):

```bash
# Install tkinter (standard Python interface to the Tcl/Tk GUI toolkit)
sudo apt-get install python3-tk

# Install dependencies
pip install -r requirements.txt
```

You can simply run the app with
```bash
python3 main.py
```

## References
<a id="1">[1]</a> 
M. Purohit, Z. Svitkina, and R. Kumar, “Improving online algorithms
via ml predictions,” in Advances in Neural Information Processing
Systems, S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-
Bianchi, and R. Garnett, Eds., vol. 31. Curran Associates, Inc.,
2018. [Online]. Available: https://proceedings.neurips.cc/paper/2018/file/73a427badebe0e32caa2e1fc7530b7f3-Paper.pdf. <br />
<a id="2">[2]</a> 
 A. R. Karlin, M. Manasse, L. Rudolph and D. Sleator. Competitive snoopy caching. Algorithmica, 3(1): 79-119, 1988. <br />
<a id="3">[3]</a>
 A. R. Karlin, M. S. Manasse, L. A. McGeoch, and S. Owicki. Competitive randomized algorithms for non-uniform problems. In Proceedings of the First Annual ACM-SIAM Symposium on Discrete Algorithms, San Francisco, CA, 22–24 January 1990, pp. 301-309. Also in Algorithmica, 11(6): 542-571, 1994. http://courses.csail.mit.edu/6.895/fall03/handouts/papers/karlin.pdf. <br />
 
