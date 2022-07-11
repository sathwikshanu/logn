#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:59:06 2022

@author: sathwik
"""

from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class Package(BaseModel):
    name:str
    number:str    
    description:Optional[str] = None

app=FastAPI()

@app.get("/")
async def hello_sathwik():
    return{"hello":"sathwik"}

 #path parameter
@app.get("/component/{component_id}")
async def get_component(component_id):
    return{"component_id":component_id}

#query parameter
@app.get("/component/")
async def read_component(number: int,text: str):
    return {"number": number,"text": text}

#query parameter
@app.post("/package/")
async def make_Package(package: Package):
    return package

@app.post("/package/{priority}")
async def make_package(priority:int,package:Package,value:bool):
    return {"priority":priority,**package.dict(),"value":value}










