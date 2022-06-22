import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
APP_DIR = os.path.join(BASE_DIR, "app/")

#configuration for tools
LOCAL_STORAGE_DIR = os.path.join(BASE_DIR, "files/")
if not os.path.exists(LOCAL_STORAGE_DIR):
    os.mkdir(LOCAL_STORAGE_DIR)

LOCAL_TEMPLATE_DIR = os.path.join(LOCAL_STORAGE_DIR, "templates/")
if not os.path.exists(LOCAL_TEMPLATE_DIR):
    os.mkdir(LOCAL_TEMPLATE_DIR)

LOCAL_COMPILED_DIR = os.path.join(LOCAL_STORAGE_DIR, "compiled/")
if not os.path.exists(LOCAL_COMPILED_DIR):
    os.mkdir(LOCAL_COMPILED_DIR)

REMOTE_STORAGE_DIR = os.getenv("REMOTE_STORAGE_DIR")
REMOTE_TEMPLATE_DIR = os.path.join(REMOTE_STORAGE_DIR, "templates/")
REMOTE_COMPILED_DIR = os.path.join(REMOTE_STORAGE_DIR, "compiled/")

#configuration for API
api_version = 1

#configuration for disk.yandex.com API
YANDEX_DISK_API_TOKEN = os.getenv("API_TOKEN")
