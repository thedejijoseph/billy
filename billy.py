# project summary in readme

import random, string
from storage import InMemory


class User:
    def __init__(self, email:str = None, name: str = None, storage=InMemory):
        """User object holding reference to user information including:
        name, email address, topics subscribed to, and any other additional info.
        """

        self.email = email
        self.name = name
        self.topics = []
        self.storage = storage()

        if self._user_exists_():
            self._fetch_user_data_()
        else:
            self.create_user(email, name)

    def _user_exists_(self):
        if self.storage.get_user(self.email):
            return True
        return False
    
    def _fetch_user_data_(self):
        user = self.storage.get_user(self.email)
        self.email = user.get('email')
        self.name = user.get('name', None)
        self.topics = user.get('topics', [])

    def create_user(self, email: str, name: str):
        """Create user by recording given data and instatiating User)."""
        
        self.storage.create_user(email=email, name=name, topics=[])
        # in an ideal world, this function could be returning a unique id
        # for the user that was just created.

    def subscribe_to(self, topic_id):
        """Add user to Topic's mailing list."""
        # confirm that user has been created
        pass
    
    def unsubscribe_from(self, topic_id):
        """Remove user from Topic's mailing list."""
        # confirm that user has been created
        pass

    def unsubscribe_from_all(self):
        """Remove user from all topics subscribed to."""
        # confirm that user has been created
        pass
    
    def get_subscriptions(self):
        """List of all topics user is subscribed to."""
        pass


class Topic:
    def __init__(self, topic_id):
        self.id = topic_id
        self.title = None
        self.desc = None
        self.users = []

    def add_user(self, email):
        # subscribe a user to this topic on their behalf
        self.users.append(email)
        print(f'User <{email}> has successfully subscibed to {self.title}.')
        return

    def remove_user(self, email):
        # remove said user from this topic's list
        self.users.remove(email)
        print(f'User <{email} has been successfully unsubscribed from {self.title}.')
        return

    def remove_all_users(self):
        # remove all user's subscribed to this list
        if len(self.users) < 15:
            for user in self.users:
                self.remove_user(user)
        else:
            self.users = []
            print('All users have been unsubscribed from this Topic.')
        
        return
