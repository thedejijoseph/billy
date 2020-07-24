
class Storage:
    """Implement specific functions to save and retrieve data
    from preferred platform/mechanism.
    """
    def __init__(self):
        pass

    def create_user(self, **kwargs):
        """Should implement methods and error resolution
        necessary to create records for a new user in preferred
        storage medium.
        """
        pass

    def get_user(self, **kwargs):
        """Should implement methods and error resolution
        neccessary to retreive recorods of a given user from
        storage medium.
        """
        pass

class InMemory(Storage):
    """Implement storage facility using Python dictionaries in-memory.
    """

    # class wide instance of database (source of truth)
    DB = {}

    def __init__(self):
        self.name = 'InMemory Storage'
        self.object_wide = {}
    
    def create_user(self, **kwargs):
        """Creates a record for a new user with the given email as unique key.
        """
        email = kwargs.get('email')
        self.DB[email] = kwargs
    
    def get_user(self, email: str):
        """Retrieves all records of a user identified by email.
        If user does not exist, None is returned.
        """
        return self.DB.get(email, None)
    
    def update_user(self, email: str, **kwargs):
        """Update records for user."""
        self.DB[email].update(kwargs)
    
    def delete_user(self, email: str):
        """Delete the records for user."""
        del self.DB[email]
    