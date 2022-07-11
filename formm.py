#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""
from fastapi import FastAPI,Form

app=FastAPI()

@app.post("/language/")
async def language(name:str = Form(...),type: str =Form(...)):
    return {"name": name,"type":type}
