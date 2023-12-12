# -------------------------------------------------------------#
#   Here we manage the app imports                             #
# -------------------------------------------------------------#
import os

from app import app

# -------------------------------------------------------------#
#   This runs the App with settings given                      #
# -------------------------------------------------------------#

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=os.environ.get('PORT', 5000)
    )