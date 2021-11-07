from flask import Flask, redirect, Markup, url_for, session, request, jsonify
from flask import render_template

import pprint
import os
import json
import sys
from datetime import datetime, date, timedelta
from pytz import timezone
import pytz

app = Flask(__name__)

@app.route('/') 
def render_main():
  grid = []
  with open('windturbine.json') as d:
    data = json.load(d)
  grid_code = ''
  row = 0    
  square = 0
  while row < 15:
    grid_code += '<tr>'
    while square < 24:
      grid_code += '<td>'
      if chr(row + 65) + str(square + 1) in data:
        grid_code += ('<button class="square-button" data-placement="auto right" title="' +
                      data['coordinates'] + '" data-toggle="popover" data-trigger="focus" data-content="Wind Speed 100m (m/s): ' +
                      str(data['100wind']) + '<br>Wind Speed 150m (m/s): ' + str(data['150wind']) + '<br>Wind Speed 200m (m/s): ' + 
                      str(data['200wind']) + '" data-toggle="popover" data-trigger="focus" data-content="popover"></button>')
      grid_code += '</td>'
      square += 1
    grid_code += '</tr>'
    square = 0
    row += 1
  return render_template('main.html', test = Markup(grid_code))

if __name__ == "__main__":
    app.run()
