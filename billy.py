# project summary in readme

import random, string

USERS = []
TOPICS = []

class User:
    def __init__(self, email):
        # return a User object made with given properties
        # an external create_user method will be used to create user accounts
        # and a get_user method used to retrieve
        # user_exists method to confirm availability
        
        self.email = email
        self.topics = topics
        self.name = None

    def subscribe_to(self, topic_id):
        # add this user to given topic's subscription list
        # return message saying whether subscription was sucessful or not

        return Topic(topic_id).add_user(self.email)
    
    def unsubscribe_from(self, topic_id):
        # remove this user's email from the topic's subscribtion list
        return Topic(topic_id).remove_user(self.email)

    def unsubscribe_from_all(self):
        # remove user from all topic list
        for topic_id in self.topics:
            Topic(topic_id).remove_user(self.email)
        return
    
    def get_subscriptions(self):
        # get a list of topic_ids this user is subscribed to
        # value should also be stored in self.topics
        return self.topics

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

    def remove_user(self, eamil):
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

def create_user(email, name):
    if user_exists(email):
        print(f'Account with email address <{email}> already exists.')
        return None
    
    user = User(email)
    user.name = name
    USERS.append(user)
    return user

def get_user(email):
    if not user_exists(email):
        print(f'Account with email address <{email}> does not exist.')
        return None
    
    for user in users:
        if user.email == email:
            return user
        else:
            print(f'For some reason, we could not find an account for <{email}>.')
            return None

def user_exists(email):
    for user in users:
        if user.email == email:
            return True
    return False

def create_topic(title, desc=None):
    random_id = ''.join(random.choices(string.ascii_lowercase, k=4))
    topic = Topic(random_id)
    topic.title = title
    topic.desc = desc
    TOPICS.append(topic)
    return Topic

def get_topic(topic_id):

    pass

def topic_exists(topic_id):
    

