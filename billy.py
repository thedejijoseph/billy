# project summary in readme


from storage import InMemory


class User:
    """User object holding reference to user information including:
    name, email address, topics subscribed to, and any other additional info.
    """
    def __init__(self, email:str = None, storage=InMemory):
        self.email = email
        self.storage = storage()

        if self._user_exists_():
            self._fetch_user_data_()

    def _user_exists_(self):
        if self.storage.get_user(self.email):
            return True
        return False
    
    def _fetch_user_data_(self):
        user = self.storage.get_user(self.email)
        self.email = user.get('email')
        self.name = user.get('name', None)

    def create_user(self, email: str, name: str):
        """Create user by recording given data and instatiating User."""
        
        self.storage.create_user(email=email, name=name)
        self._fetch_user_data_()
        return self

    def subscribe_to(self, topic_id):
        """Add user to Topic's mailing list."""
        if not self._user_exists_():
            print(f'User <{self.email}> does not exist.')
            return
        topic = Topic(topic_id=topic_id)
        topic.add_user(self.email)
    
    def unsubscribe_from(self, topic_id):
        """Remove user from Topic's mailing list."""
        if not self._user_exists_():
            print(f'User <{self.email}> does not exist.')
            return
        topic = Topic(topic_id=topic_id)
        topic.remove_user(self.email)

    def unsubscribe_from_all(self):
        """Remove user from all topics subscribed to."""
        if not self._user_exists_():
            print(f'User <{self.email}> does not exist.')
            return
        topics = Topic().get_user_topics(self.email)
        for topic in topics:
            Topic(topic_id=topic).remove_user(self.email)
    
    def get_subscriptions(self):
        """List of all topics user is subscribed to."""
        if not self._user_exists_():
            print(f'User <{self.email}> does not exist.')
            return
        topics = Topic().get_user_topics(self.email)
        return topics


class Topic:
    """Custom object representing a topic and implementing methods
    necessary to manipulate it's attributes.
    """
    def __init__(self, topic_id: str = None, storage=InMemory):
        self.id = topic_id
        self.storage = storage()

        if self._topic_exists_():
            self._fetch_data_()
    
    def _topic_exists_(self):
        if self.storage.get_topic(self.id):
            return True
        return False

    def _fetch_data_(self):
        topic = self.storage.get_topic(self.id)
        self.title = topic.get('topic_id')
        self.desc = topic.get('desc', None)
        self.users = topic.get('users', [])

    def create_topic(self, title: str, desc: str = None):
        """Create a new topic by recording given data and instatiating Topic.
        """
        self.storage.create_topic(title=title, desc=desc, users=[])
        self._fetch_data_()
        return self
    
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
