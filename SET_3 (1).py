#!/usr/bin/env python
# coding: utf-8

# In[63]:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):
    if (to_member in social_graph[from_member]["following"]) and (from_member in social_graph[to_member]["following"]):
        status = "friends"
    elif from_member in social_graph[to_member]["following"]:
        status = "followed by"
    elif to_member in social_graph[from_member]["following"]:
        status = "follower"
    else:
        status = "no relationship"
    return status
relationship_status("@eeebeee", "@jobenilagan", social_graph)


# In[ ]:


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    counter = 0
    counter2 = 0
    vertical = ""
    diagonal = ""
    diagonal2 = ""

    
    while counter != len(board):
        if board[counter].count("X") == len(board):
            return "X"
        elif board[counter].count("O") == len(board):
            return "O"
        counter += 1

    
    counter = 0
    while counter2 != len(board):
        while counter != len(board):
            vertical += board[counter][counter2]
            counter += 1
            
        if vertical.count("X") == len(board):
            return "X"
        elif vertical.count("O") == len(board):
            return "O"
            
        vertical = ""
        counter2 += 1
        counter = 0

    
    counter = 0
    while counter != len(board):
        diagonal += board[counter][counter]
        counter+=1
    if diagonal.count("X") == len(board):
        return "X"
    elif diagonal.count("O") == len(board):
        return "O"    
    
    counter = 0
    counter2 = len(board)-1
    while counter2 != (-1):
        diagonal2 += board[counter][counter2]
        counter +=1
        counter2 -=1
    if diagonal2.count("X") == len(board):
        return "X"
    elif diagonal2.count("O") == len(board):
        return "O"

    else:
        return "NO WINNER"


# In[ ]:


legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):
    route = list(route_map.keys())
    time = 0

    from_stop = None
    for i in range(len(route)):
        if route[i][0] == first_stop:
            from_stop = i
            break

    current_stop = from_stop
    while True:
        time += route_map[route[current_stop]]["travel_time_mins"]
        
        if route[current_stop][1] == second_stop:
            break
        current_stop = (current_stop + 1) % len(route)

    return time

