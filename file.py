users = {1: {"name": "user2","transaction_id": 1,"movies": []}, 2:{"name": "user2","transaction_id": 2,"movies": [5,6]}}
movies = {1: {"name": "movie1","available": True,"price": 50,"users": [3,4]},2:{"name": "movie2","available": False,"price": 90},"users":[2,5,6]}

def rent_movie(movie_id,user_id):
    if movies[movie_id]["available"]==True:
        users[user_id]["movies"].append(movie_id)
        movies[movie_id]["available"]=False
        movies[movie_id]["users"].append(user_id)
        print("Movie Rented")
        print(users[user_id])
    else: 
        print("Movie not Available")

def return_movie(movie_id,user_id):
    if movie_id in users[user_id]["movies"]:
        users[user_id]["movies"].remove(movie_id)
        movies[movie_id]["available"]=True
        movies[movie_id]["users"].remove(user_id)
        print("Movie Returned")
        print(users[user_id])
    else: 
        print("No Movie Found with the given Id")

def report(movie_id):
    print("Report: ")
    name=movies[movie_id]["name"]
    price=movies[movie_id]["price"]
    users=movies[movie_id]["users"]
    total_rev=len(movies[movie_id]["users"])*price
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Users: {users}")
    print(f"Total Revenu: {total_rev}")
    
def add_user():
    user_id=int(input("User Id: "))
    user_name=input("User Name: ")
    users[user_id]={"name": user_name,"transaction_id": user_id,"movies": []}

print("1: Rent Movie, 2: Return Movie, 3: Report, 4: Add User")
opt=int(input("Option: "))
movie_id=int(input("Movie Id: "))
user_id=int(input("User Id: "))
if opt==1:
    rent_movie(movie_id,user_id)
if opt==2:
    return_movie(movie_id,user_id)
    
if opt==3:
    report(movie_id)

if opt==4:
    add_user()
    print(users)
