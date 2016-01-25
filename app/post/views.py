from flask import Blueprint, render_template, request, redirect
from app.core.db import database
from models import Post, Comment, Like

post_views = Blueprint('post', __name__, template_folder='../../templates')
