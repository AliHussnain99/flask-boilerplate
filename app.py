from core.settings import *
from core.utils.helpers import get_env_variable

if __name__ == '__main__':
    app.run(debug=get_env_variable('FLASK_DEBUG'), host="0.0.0.0", port=5000)
