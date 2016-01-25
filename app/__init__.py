from app.core.helper import create_app
from app.core.db import database
from app.user.views import user_views
from app.post.views import post_views
from app.core.views import coreView
from app.core.bcrypt import bcrypt

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'

app = create_app(config)
database.init_app(app)
bcrypt.init_app(app)

# register blueprint
app.register_blueprint(coreView)
app.register_blueprint(user_views, url_prefix="/user")
app.register_blueprint(post_views, url_prefix="/post")
