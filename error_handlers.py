from app import app
from flask import flash, redirect, url_for

# - Error Handler ---------------------------------------------#
#   This handles if the site experiences a 404 error           #
# -------------------------------------------------------------#

@app.errorhandler(404)
def error_404(exception):
    flash(u"Oops! seems we couldn't find that", 'danger')
    return redirect(url_for('index'))


# - Error Handler ---------------------------------------------#
#   This handles if the site experiences a 403 error           #
# -------------------------------------------------------------#

@app.errorhandler(403)
def error_403(exception):
    flash(u"You are not allowed to perform that action!", 'danger')
    return redirect(url_for('index'))

# - Error Handler ---------------------------------------------#
#   This handles if the site experiences a 405 error           #
# -------------------------------------------------------------#

@app.errorhandler(405)
def error_405(exception):
    flash(u"Method is not allowed", 'danger')
    return redirect(url_for('index'))