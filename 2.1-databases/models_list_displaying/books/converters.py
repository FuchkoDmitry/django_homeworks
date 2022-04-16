from datetime import datetime


class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    # format = '%Y-%m-%d'

    # def to_python(self, value: str) -> datetime:
    def to_python(self, value):
        # return datetime.strptime(value, self.format)
        return value

    # def to_url(self, value):
    def to_url(self, value):
        # return value.strftime(self.format)
        return value.__str__()
