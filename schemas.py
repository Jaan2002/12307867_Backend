from pydantic import BaseModel
from typing import List, Optional

class TaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    is_completed: Optional[bool] = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

class TaskListResponse(BaseModel):
    tasks: List[TaskResponse]

class BulkTaskCreate(BaseModel):
    tasks: List[TaskCreate]

class BulkTaskDelete(BaseModel):
    tasks: List[dict]
