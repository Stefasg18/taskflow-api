from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.dependencies import current_user
from app.models import Task, User
from app.schemas import TaskCreate, TaskUpdate, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("", response_model=list[TaskOut])
async def list_tasks(status: str | None = None, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    q = select(Task).where(Task.owner_id == user.id)
    if status: q = q.where(Task.status == status)
    return (await db.execute(q.order_by(Task.id.desc()))).scalars().all()

@router.post("", response_model=TaskOut, status_code=201)
async def create_task(data: TaskCreate, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    task = Task(**data.model_dump(), owner_id=user.id)
    db.add(task); await db.commit(); await db.refresh(task)
    return task

@router.patch("/{task_id}", response_model=TaskOut)
async def update_task(task_id: int, data: TaskUpdate, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    task = await db.get(Task, task_id)
    if not task or task.owner_id != user.id: raise HTTPException(404, "Task not found")
    for k, v in data.model_dump(exclude_unset=True).items(): setattr(task, k, v)
    await db.commit(); await db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    task = await db.get(Task, task_id)
    if not task or task.owner_id != user.id: raise HTTPException(404, "Task not found")
    await db.delete(task); await db.commit()
