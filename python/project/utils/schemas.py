from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    """Схема проверки ответа от эндпоинта /posts/{id}"""
    userId: int
    id: int
    title: str
    body: str = Field(min_length=1)  # Проверяем, что тело поста не пустое