from gurobipy import *
# there are 3 techs and 3 jobs 
noItin = 16
noFlight = 4
# initialize the reward data
rewards = [ 0 for i in range ( noItin )  ] 
rewards[ 0 ] = 200
rewards[ 1 ] = 230
rewards[ 2 ] = 320
rewards[ 3 ] = 420 
rewards[ 4 ] = 400
rewards[ 5 ] = 490
rewards[ 6 ] = 250
rewards[ 7 ] = 290
rewards[ 8 ] = 410 
rewards[ 9 ] = 550
rewards[ 10 ] = 450 
rewards[ 11 ] = 550
rewards[ 12 ] = 200
rewards[ 13 ] = 230
rewards[ 14 ] = 250 
rewards[ 15 ] = 300

# initialize the capacity data
capacity = [ 0 for j in range ( noFlight )  ] 
capacity[ 0 ] = 200
capacity[ 1 ] = 200
capacity[ 2 ] = 200
capacity[ 3 ] = 200

# initialize the demand constraints
demand = [  0 for j in range ( noItin )   ] 
demand[ 0 ] = 25
demand[ 1 ] = 20
demand[ 2 ] = 55
demand[ 3 ] = 40 
demand[ 4 ] = 65
demand[ 5 ] = 25
demand[ 6 ] = 24
demand[ 7 ] = 16
demand[ 8 ] = 65
demand[ 9 ] = 50
demand[ 10 ] = 40
demand[ 11 ] = 35
demand[ 12 ] = 21
demand[ 13 ] = 20
demand[ 14 ] = 25
demand[ 15 ] = 14
# initialize the incidence matrix
A = [ [ 0 for i in range ( noItin ) ] for j in range ( noFlight ) ] 
A[ 0 ][ 0 ] = 1
A[ 0 ][ 1 ] = 1 
A[ 0 ][ 2 ] = 1 
A[ 0 ][ 3 ] = 1 
A[ 0 ][ 4 ] = 1 
A[ 0 ][ 5 ] = 1 
A[ 1 ][ 6 ] = 1 
A[ 1 ][ 7 ] =1
A[ 1][ 8 ] = 1 
A[ 1 ][ 9 ] = 1
A[ 1 ][ 10 ] = 1
A[ 1 ][ 11 ] = 1
A[ 2 ][ 2 ] = 1
A[ 2 ][ 3 ] = 1
A[ 2 ][ 8 ] = 1
A[ 2 ][ 9 ] = 1
A[ 2 ][ 12 ] = 1
A[ 2 ][ 13 ] = 1
A[ 3 ][ 4 ] = 1
A[ 3 ][ 5 ] = 1
A[ 3 ][ 10 ] = 1
A[ 3 ][ 11 ] = 1
A[ 3 ][ 14 ] = 1
A[ 3 ][ 15 ] = 1

# create a new model
myModel = Model( "HW_2_Problem_1" )

# create decision variables and store them in the array myVars
myVars = [  0 for i in range ( noItin )  ] 
for i in range( noItin ):
        curVar = myModel.addVar( vtype = GRB.CONTINUOUS , name = "x" + str( i ) )
        myVars[ i ] = curVar

# integrate decision variables into the model 
myModel.update()

# create a linear expression for the objective 
objExpr = LinExpr()
for i in range( noItin ):
        objExpr += rewards[ i ] * myVars[i] 
myModel.setObjective( objExpr , GRB.MAXIMIZE )

        
# create constraints so that each flight does not exceed capacity 
for j in range( noFlight ):
    constExpr = LinExpr()
    for i in range( noItin ):
        constExpr += 1 * myVars[ i ]*A[j][i] 
    myModel.addConstr( lhs = constExpr , sense = GRB.LESS_EQUAL , rhs = capacity[j]
, name = "c" + str( j ) )
    

# create constraints so that each itinerary does not exceed demand
for i in range( noItin ):
    constExpr = LinExpr() 
    constExpr = myVars[ i ]
    myModel.addConstr( lhs = constExpr , sense = GRB.LESS_EQUAL , rhs = demand[i] ,
    name = "d" + str( i ) )
        
# integrate objective and constraints into the model 
myModel.update()
# write the model in a file to make sure it is constructed correctly 
myModel.write( filename = "FinalOutput.lp" )
# optimize the model 
myModel.optimize()
# print optimal objective and optimal solution
print("\nOptimal Objective: " + str( myModel.ObjVal ) )
print( "\nOptimal Solution:" )
allVars = myModel.getVars()
for curVar in allVars:
    print ( curVar.varName + " " + str( curVar.x ) )
    
# print optimal dual solution 
print( "\nOptimal Dual Solution:" ) 
myConsts = myModel.getConstrs() 
for curConst in myConsts:
    print ( curConst.constrName + " " + str( curConst.pi ) )