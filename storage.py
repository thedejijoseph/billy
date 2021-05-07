
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
    DB = {
        "topics": {},
        "users": {}
    }

    def __init__(self):
        self.name = 'InMemory Storage'
        self.object_wide = {}
    
    def create_user(self, email, data):
        """Creates a record for a new user with the given email as unique key.
        """
        self.DB['users'][email] = data
        return self.get_user(email)
    
    def get_user(self, email: str):
        """Retrieves all records of a user identified by email.
        If user does not exist, None is returned.
        """
        return self.DB['users'].get(email, None)
    
    def update_user(self, email: str, data):
        """Update records for user."""
        self.DB['users'][email].update(data)
    
    def delete_user(self, email: str):
        """Delete the records for user."""
        del self.DB['users'][email]
    
    def get_topic(self, topic_id):
        return self.DB['topics'].get(topic_id, None)
    
    def create_topic(self, topic_id, data):
        self.DB['topics'][topic_id] = data
        return self.get_topic(topic_id)
    
    def update_topic(self, topic_id, data):
        self.get_topic(topic_id).update(data)
    
    def all_topics(self):
        return self.DB['topics'].items()
    
    def __repr__(self) -> str:
        print(self.DB)
        topic_count = len(self.DB['topics'].items())
        user_count = len(self.DB['users'].items())
        return f"Topics: {topic_count}; Users: {user_count}"
