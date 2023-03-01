from gurobipy import *
# there are 3 techs and 3 jobs 
noItin = 8
noFlight = 2
# initialize the reward data
rewards = [ 0 for i in range ( noItin )  ] 
rewards[ 0 ] = 425
rewards[ 1 ] = 350
rewards[ 2 ] = 625
rewards[ 3 ] = 450
rewards[ 4 ] = 400
rewards[ 5 ] = 300
rewards[ 6 ] = 300
rewards[ 7 ] = 300

# initialize the capacity data
capacity = [ 0 for j in range ( noFlight )  ] 
capacity[ 0 ] = 100
capacity[ 1 ] = 100
# initialize the demand constraints
demand = [  0 for j in range ( noItin )   ] 
demand[ 0 ] = 30
demand[ 1 ] = 50
demand[ 2 ] = 40
demand[ 3 ] = 65
demand[ 4 ] = 50
demand[ 5 ] = 80
# initialize the incidence matrix
A = [ [ 0 for i in range ( noItin ) ] for j in range ( noFlight ) ] 
A[ 0 ][ 0 ] = 1
A[ 0 ][ 1 ] = 1 
A[ 0 ][ 2 ] = 1 
A[ 0 ][ 3 ] = 1 
A[ 1 ][ 2 ] = 1 
A[ 1 ][ 3 ] =1
A[ 1][ 4 ] = 1 
A[ 1 ][ 5 ] = 1
# create a new model
myModel = Model( "RMExample" )
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
# create constraints so that each itinerary does not exceed demand
for i in range( noItin ):
    constExpr = LinExpr() 
    constExpr = myVars[ i ]
    myModel.addConstr( lhs = constExpr , sense = GRB.LESS_EQUAL , rhs = demand[i] ,
name = "d" + str( i ) )
# create constraints so that each flight does not exceed capacity 
for j in range( noFlight ):
    constExpr = LinExpr()
    for i in range( noItin ):
        curVar = myVars[ i ]*A[j][i]
        constExpr += 1 * curVar 
    myModel.addConstr( lhs = constExpr , sense = GRB.LESS_EQUAL , rhs = capacity[j]
, name = "c" + str( j ) )
# integrate objective and constraints into the model 
myModel.update()
# write the model in a file to make sure it is constructed correctly 
myModel.write( filename = "testOutput.lp" )
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