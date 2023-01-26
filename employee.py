from pydantic import BaseModel

class MyBaseModel(BaseModel):
    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))

class Employee(MyBaseModel):

    promoted: int
    review: int
    projects: int
    tenure: int
    satisfaction: int
    bonus: int
    avg_hrs_month: int