from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask(__name__)

connection = sqlite3.connect('database.db')




