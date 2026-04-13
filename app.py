from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = '/home/claude/bears.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def rows_to_list(rows):
    return [dict(r) for r in rows]

@app.route('/api/roster')
def roster():
    db = get_db()
    rows = db.execute("SELECT * FROM roster ORDER BY position, name").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

@app.route('/api/passing')
def passing():
    db = get_db()
    rows = db.execute("SELECT DISTINCT player, att, comp, yds, comp_pct, yds_per_att, td, int_thrown, sck, rate FROM passing ORDER BY yds DESC").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

@app.route('/api/rushing')
def rushing():
    db = get_db()
    rows = db.execute("SELECT DISTINCT player, att, yds, yds_per_att, long, td FROM rushing ORDER BY yds DESC").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

@app.route('/api/receiving')
def receiving():
    db = get_db()
    rows = db.execute("SELECT DISTINCT player, rec, yds, yds_per_rec, long, td FROM receiving ORDER BY yds DESC").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

@app.route('/api/tackles')
def tackles():
    db = get_db()
    rows = db.execute("SELECT DISTINCT player, total, solo, assist, sck, forced_fmbl FROM tackles ORDER BY total DESC").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

@app.route('/api/interceptions')
def interceptions():
    db = get_db()
    rows = db.execute("SELECT DISTINCT player, int_caught, yds, yds_per_ret, long, tds FROM interceptions ORDER BY int_caught DESC").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

@app.route('/api/field_goals')
def field_goals():
    db = get_db()
    rows = db.execute("SELECT DISTINCT player, fg_1_19, fg_20_29, fg_30_39, fg_40_49, fg_50_59, fg_60_plus FROM field_goals").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

@app.route('/api/stats/summary')
def summary():
    db = get_db()
    roster_count = db.execute("SELECT COUNT(*) as c FROM roster").fetchone()['c']
    top_passer = db.execute("SELECT player, yds, td FROM passing ORDER BY yds DESC LIMIT 1").fetchone()
    top_rusher = db.execute("SELECT player, yds, td FROM rushing ORDER BY yds DESC LIMIT 1").fetchone()
    top_receiver = db.execute("SELECT player, yds, td FROM receiving ORDER BY yds DESC LIMIT 1").fetchone()
    top_tackler = db.execute("SELECT player, total FROM tackles ORDER BY total DESC LIMIT 1").fetchone()
    db.close()
    return jsonify({
        "roster_count": roster_count,
        "top_passer": dict(top_passer) if top_passer else None,
        "top_rusher": dict(top_rusher) if top_rusher else None,
        "top_receiver": dict(top_receiver) if top_receiver else None,
        "top_tackler": dict(top_tackler) if top_tackler else None,
    })

@app.route('/api/positions')
def positions():
    db = get_db()
    rows = db.execute("SELECT position, COUNT(*) as count FROM roster GROUP BY position ORDER BY count DESC").fetchall()
    db.close()
    return jsonify(rows_to_list(rows))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
