from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from research_and_analysis.database.db_config import SessionLocal, User, hash_password, verify_password
from research_and_analysis.api.services.re
