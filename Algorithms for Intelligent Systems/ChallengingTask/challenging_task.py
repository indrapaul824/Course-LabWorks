#!/usr/bin/env python
# coding: utf-8

# # Challenging Task 1 - Group Task
# 
# For Algorithm for Intelligent Systems - CSA4001 - B11+B12 slot
# 
# Group Details:
# - Raghav Agarwal, 19MIM10024
# - Indrashis Paul, 19MIM10046
# - Shobhit Vatsya, 19MIM10040
# 
# ----

# # Simulated Annealing

# ### 1.0.1 Importing Libraries

# In[1]:


from numpy import asarray, exp
from numpy.random import randn, rand, seed
from matplotlib import pyplot


# ### 1.0.2 Define objective function

# In[2]:


def objective(step):
    return step[0] ** 2.0


# ### 1.0.3 Define simulated annealing algorithm

# In[3]:


def sa(objective, area, iterations, step_size, temperature):
    # create initial point
    start_point = area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])
    # evaluate initial point
    start_point_eval = objective(start_point)
    # Assign previous and new solution to previous and new_point_eval variable
    mia_start_point, mia_start_eval = start_point, start_point_eval
    outputs = []
    for i in range(iterations):
        # First step by mia
        mia_step = mia_start_point + randn( len( area ) ) * step_size
        mia_step_eval = objective(mia_step)
        if mia_step_eval < start_point_eval:
            start_point, start_point_eval = mia_step, mia_step_eval
            #Append the new values into the output list
            outputs.append(start_point_eval)
            print('Acceptance Criteria = %.5f' % mac, " ", 'iteration Number = %d' % i, " ", 'best_so_far = %.5f' % start_point, " ", 'new_best = %.5f' % start_point_eval)
        difference = mia_step_eval - mia_start_eval
        t = temperature / float(i + 1)
        # calculate Metropolis Acceptance Criterion / Acceptance Probability
        mac = exp(-difference / t)
        # check whether the new point is acceptable
        if difference < 0 or rand() < mac:
            mia_start_point, mia_start_eval = mia_step, mia_step_eval
    return [start_point, start_point_eval, outputs]


# In[4]:


seed(1)
# define the area of the search space
area = asarray([[-6.0, 6.0]])

# initial temperature
temperature = 12
# define the total iterations
iterations = 1200
# define the maximum step size
step_size = 0.1

# perform the simulated annealing search
start_point, output, outputs = sa(objective, area, iterations, step_size, temperature)


# ### 1.0.4 Plotting the values

# In[5]:


pyplot.plot(outputs, 'ro-')
pyplot.xlabel('Improvement Value')
pyplot.ylabel('Evaluation of Objective Function')
pyplot.show()


# ----- End of Group Activity -----

# # Challenging Task 2 - Individual Task
# ---
# # PROLOG

# ### Q1. Print 1 to 10 using Prolog
# 
# ![prolog1.png](./prolog1.png)
# ---
# ---
# 
# ### Q2. Print Factorial of the given number using Prolog
# 
# ![prolog2.png](./prolog2.png)
# ---
# ---
# 
# ### Q3. Print Fibonacci Series upto a given number using Prolog
# 
# ![prolog3.png](./prolog3.png)
# ---
# ---
