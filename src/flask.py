from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask("Notes App")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

