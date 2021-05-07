# project summary in readme


import string, random
from storage import InMemory

STORAGE = InMemory()
class User:
    """User object holding reference to user information including:
    name, email address, topics subscribed to, and any other additional info.
    """
    def __init__(self, email:str, name: str = "", storage=STORAGE):
        self._email = email
        self._name = name
        self.storage = storage

        self._load_user()
    
    def _load_user(self):
        user = self.storage.get_user(self.email)
        if not user:
            print(f'Creating new user with email <{self.email}>')
            data = {
                "email": self.email,
                "name": self.name
            }
            user = self.storage.create_user(self.email, data)
        
        user = self.storage.get_user(self.email)
        for key, value in user.items():
            setattr(self, f'_{key}', value)
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
        self.storage.update_user(self.email, {"email": value})

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        self.storage.update_user(self.email, {"name": value})
    
    def __repr__(self) -> str:
        if self.name:
            return f"{self.name} <{self.email}>"
        else:
            return f"User <{self.email}>"

    def subscribe_to(self, topic_id):
        """Add user to Topic's mailing list."""
        topic = Topic.from_id(topic_id)
        topic.add_user(self.email)
    
    def unsubscribe_from(self, topic_id):
        """Remove user from Topic's mailing list."""
        if not self._user_exists_():
            print(f'User <{self.email}> does not exist.')
            return
        topic = Topic.from_id(topic_id)
        topic.remove_user(self.email)

    def unsubscribe_from_all(self):
        """Remove user from all topics subscribed to."""
        topics = self.storage.all_topics()
        for topic in topics:
            # we could check if a user is subscribed to the
            # topic first.. or we could just throw a blind swing 
            Topic.from_id(topic['topic_id']).remove_user(self.email)
    
    def get_subscriptions(self):
        """List of all topics user is subscribed to."""
        topics = Topic.get_user_topics(self.email)
        return [topic['topic_id'] for topic in topics if self.email in topic['users']]


class Topic:
    """Custom object representing a topic and implementing methods
    necessary to manipulate it's attributes.
    """
    def __init__(
        self, title: str = "", 
        desc: str = "", storage=STORAGE):

        self.title = title
        self.desc = desc
        self.storage = storage

        self._load_topic()
    
    def add_user(self, email):
        """Subscribe a user to this topic"""
        self.users.append(email)
        self.storage.update_topic(self.id, {"users": self.users})
        print(f'User <{email}> has successfully subscibed to {self.title}.')
        return

    def remove_user(self, email):
        """Remove a user from this list"""
        self.users.remove(email)
        self.storage.update_topic(self.id, {"users": self.users})
        print(f'User <{email}> has been successfully unsubscribed from {self.title}.')
        return

    def remove_all_users(self):
        """Remove all users subscribed to this list"""
        self.users = []
        self.storage.update_topic(self.id, {"users": self.users})
        print('All users have been unsubscribed from this Topic.')
        return
    
    @classmethod
    def from_id(self, topic_id):
        """Get a Topic instance from its ID"""
        topic = Topic()._load_topic(topic_id)
        return topic
    
    def _load_topic(self, topic_id=None):
        if not topic_id:
            # creating a new topic
            pool = string.ascii_lowercase + string.digits
            topic_id = "".join(random.choices(pool, k=5))
            data = {
                "topic_id": topic_id,
                "title": self.title,
                "desc": self.desc,
                "users": []
            }
            topic = self.storage.create_topic(topic_id, data)
            return self._load_topic(topic_id)
        
        topic = self.storage.get_topic(topic_id)
        if not topic:
            print(f'Topic  with ID "{topic_id}" does not exist.')
            return
        
        self.id = topic_id
        for key, value in topic.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        return f"{self.title} <{self.id}>"
