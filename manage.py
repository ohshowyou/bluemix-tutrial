import os
from flaskr import app
port = os.getenv('PORT', '5000')
app.run(host='0.0.0.0', port=int(port))
# testtest
