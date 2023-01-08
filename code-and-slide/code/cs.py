student=[("ali", ["CS", "ph"]),
         ("amir", ["CS", "ms"])
        ]
n=0
for ( nm , co ) in student :
    for i in co :
        if i == "CS" :
            n = n+1
print ( "n" , n )
