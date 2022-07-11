#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:40:44 2022

@author: sathwik
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List
from fastapi import HTTPException

class Todo(BaseModel):
    
    name: str
    due_date:str
    description:str
    
app=FastAPI(title="Todo API")

#create,read,Update, Delete

store_todo = []

@app.get("/")
async def home():
    return {"hello":"sathwik"}

@app.post("/todo/")
async def create_todo(todo:Todo):
    store_todo.append(todo)
    return todo

@app.get("/todo", response_model=List[Todo])
async def get_all_todo():
    return store_todo

@app.get('/todo/{id}')
async def get_todo(id: int):
    
    try:
        
        return store_todo[id]
    except:
        
        raise HTTPException(status_code=404, detail="Todo")

@app.put("/todo/{id}")
async def Update_todo(id: int,todo: Todo):
    
    try:
        
        store_todo[id] = todo
        return store_todo[id]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo")
        
@app.delete("/todo/{id}")
async def delete_linux(id: int):
    
    try:
        
        obj =store_todo[id]
        store_todo=pop(id)
        return obj
    
    except:
        
        
        raise HTTPException(status_code=404, detail="Todo")



















