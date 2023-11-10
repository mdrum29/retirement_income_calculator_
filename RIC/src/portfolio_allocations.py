def getAllocation(risk):
    
    if risk == "VERY_CONSERVATIVE" or int(risk) == 1:
        v_con = {"stock_allocation": 0, "bond_allocation": 1}
        return v_con
    
    elif risk == "CONSERVATIVE" or int(risk) == 2:
        con = {"stock_allocation": .25, "bond_allocation": .75}
        return con
    
    elif risk == "MODERATE" or int(risk) == 3:
        mod = {"stock_allocation": .6, "bond_allocation": .4}
        return mod
    
    elif risk == "AGGRESSIVE" or int(risk) == 4:
        agg = {"stock_allocation": .8, "bond_allocation": .2}
        return agg
    
    elif risk == "VERY_AGGRESSIVE" or int(risk) == 5:
        v_agg = {"stock_allocation": 1, "bond_allocation": 0}
        return v_agg
    
    else:
        raise Exception ("Invalid Risk Tolerance Value")
    