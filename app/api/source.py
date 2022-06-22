from app.app_config import *

from app.tools.yandex.disk_manager import DiskManager
from app.tools.yandex.exceptions import InvalidAuthTokenException

from app.tools.documents.document_compiler import compile_template

disk_manager = None
try:
    disk_manager = DiskManager(token=YANDEX_DISK_API_TOKEN)
except InvalidAuthTokenException as exception:
    #TODO: mailing integration
    print(exception)