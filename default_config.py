import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://gvsjrxja:3Iso9KT_bbrXpqns_8WH4NCEvoqtzce-@heffalump.db.elephantsql.com/gvsjrxja"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
UPLOADED_IMAGES_DEST = os.path.join("static", "images")  # manage root folder
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_BLOCKLIST_ENABLED = True
JWT_BLOCKLIST_TOKEN_CHECKS = [
    "access",
    "refresh",
]  # allow blocklisting for access and refresh tokens