from scipy.integrate import odeint 
import math 
import numpy as np

class name_of_your_model:
    def __init__(self):
        #Fill up with your parameters
        #Example: self.Y_XS = 0.8 #g/g

        #Initialization of state variable
        #Example: self.S0 = 18

    def rxn(self, C, t):
        #number of components (n = )
        #number of processes (m = )

        #initialize the stoichiometric matrix (e.g. s)
        #s = np.zeros((m,n))
        
        #We define each value of the matrix
        #Example: self.s[0,0]=(-1/self.Y_XS)

        #initialize the process vector (e.g. rho)
        #rho = np.zeros((m,1))

        #We define each value of the process rate vector
        ##Example: rho[0,0] = self.mu_max*(C[0]/(C[0]+self.Ks))*C[2]

        #the overall conversion rate is stoichiometric *rates
        ##Example: self.r[0,0]= self.s[0,0]*self.rho[0,0]+self.s[1,0]*self.rho[1,0]+(s[2,0]*rho[2,0])

        #Then, it is solved the mass balances, in this case discontinuous:
        ##Example: dSdt = self.r[0,0]
        return [dSdt,...]
              
    def solve(self):        
        #Create a vector that shows the initial time to solve the model
        #t = np.linspace(t0, tf)
        
        #Vector with the initial conditions of the state variables
        #C0 = [self.S0,.....]

        #The ODE solver
        #C = odeint(self.rxn, C0, t, rtol = 1e-7, mxstep= 500000)
        return t, C

#How to call the model so it is printed. 
t, C = Model().solve()
