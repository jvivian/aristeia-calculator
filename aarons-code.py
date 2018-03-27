set random as rd
set pandas as pd

dice_1 = pd.dataframe['s':[0,0,1,1,1,2],'b':[0,1,0,1,1,0],'e':[0,0,0,0,1,1]]
dice_2 = pd.dataframe['s':[0,0,1,1,1,0],'b':[0,1,0,1,1,2],'e':[0,0,0,0,1,1]]
dice_3 = pd.dataframe['s':[0,0,0,0,1,1],'b':[0,0,0,1,1,0],'e':[1,1,1,1,1,2]]
dice_4 = pd.dataframe['s':[0,1,1,-1,1,2],'b':[0,0,0,0,0,0],'e':[0,0,0,1,1,1]]
dice_5 = pd.dataframe['s':[0,0,0,0,0,0],'b':[0,0,1,-1,1,2],'e':[0,0,0,0,1,1]]
dice_6 = pd.dataframe['s':[0,0,0,0,0,0],'b':[0,0,0,1,1,1],'e':[0,0,0,0,0,0]]

#1=o, 2=b, 3=y, 4=4, 5=g, 6=bk

def function meanroll(num_1, num_2, num_3, num_4, num_5, num_6)
for x= (1,6)
    if num_x > 0 then:
    for(1,1000)
            i = rd.randint(1,6)
            stally += dice_x[1,i]/1000
            btally += dice_x[2,i]/1000
            etally += dice_x[3,i]/1000
    end if       
    
print 'the average amount of sucesses are' stally 
print 'the average amount of blocks are' btally 
print 'the average amount of specials are' etally 
end def
    
def function condprobroll(num_1, num_2, num_3, num_4, num_5, num_6)
for x= (1,6)
    if num_x > 0 then:
    for(1,1000)
            i = rd.randint(1,6)
            for n = (1,3)
            if dice_x[n,i]>0 then
                s_n += 1
                if dice_x[n,i] > 1 then
                ds_n += 1
                end if
                end if
    end if  
for z = (0,9)    
print 'probability more than' z 'success', s_n_z/1000   
print 'probability more than' z 'block', b_n_z/1000
end def    

def function attack(num_1, num_2, num_3, num_4, num_5, num_6,num_7,num_8,num_9,num_10,num_11,num_12)
    for(1,1000)
        for x=(1,6) 
            if num_x > 0 then
            i = rd.randint(1,6)
            for n = (1,3)
            atk_n += dice_x[n,i]
        for x = (7,12)
            if num_x > 0 then
            i = rd.randint(1,6)
            y = x-6
            for n = (1,3)
            def_n += dice_y[n,i]
            end if
        for n =(1,2)
            atk_net = atk_1-def_2
            def_net = def_1-atk_2
                for z = (0,9)
                if atk_net > z then
                atk_cdf_z += 1/1000 
                end if
                if def_net > z then
                def_cdf_z += 1/1000
                end if
                
for z = (0,9)
    print 'the probability of the attacker doing at least' z 'damage is' atk_cdf_z
    print 'the probability of the defender doing at least' z 'damage is' def_cdf_z
end def
            
            
