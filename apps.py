from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Data Analyst",
    'location': 'Mogadishu, Somalia',
    'Salary': '$50,000'
  },
  {
    'id': 2,
    'title': "Data Scientist",
    'location': 'Bosaso, Somalia',
    'Salary': '$80,000'
  },
  {
    'id': 3,
    'title': "Frontend Engineer",
    'location': 'Remote, Somalia',
  },
  {
    'id': 4,
    'title': "Backend Engineer",
    'location': 'Hargaysa. So',
    'Salary': '$150,000'
  },
]


@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                         company_name='Red leaf Petroleum')


@app.route("/api/jobs")
def hello_redleaf():
  return jsonify(JOBS)


# print(__name__)
if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
