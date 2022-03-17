from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name'] #DB Columns
        self.last_name = data['last_name'] #DM Columns
        self.email = data['email'] #DB Columns
        self.created_at = data['created_at'] #DB Columns
        self.updated_at = data['updated_at'] #DB Columns
    # Now we use class methods to query our database
    
    @classmethod
    def save(cls, data:dict): 
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);" #write the query in the workbench to test it 
        # database request
        user_id = connectToMySQL('users_db').query_db(query,data) #Target DB HERE city_id is variable name --> because insert query it'll return ID # of the row inserted
        return user_id
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_db').query_db(query) #THE RETURN IS A LIST OF DICTIONARIES
        # Create an empty list to append our instances of friends
        all_users = [] #becomes a list of instances
        # Iterate over the db results and create instances of cities with cls. 
        for user in results: #for dictionary(city) in list of dictionaries (results line22) grab empty list (all_cities line24) and append cls(city)
            all_users.append( cls(user) ) #[**Do NOT RETURN A LIST OF DICTIONARIES to HTML FOR THIS STACK -- RETURN A LIST OF INSTANCES]
        return all_users