class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

class Project:
    def __init__(self, project_id, name, description):
        self.project_id = project_id
        self.name = name
        self.description = description

class ModelMetrics:
    def __init__(self, metric_id, project_id, accuracy, precision, recall):
        self.metric_id = metric_id
        self.project_id = project_id
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall

class DynamicField:
    def __init__(self, field_name, field_type, value):
        self.field_name = field_name
        self.field_type = field_type
        self.value = value
