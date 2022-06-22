from typing import Optional
from typing import Dict, Tuple  

from yadisk import YaDisk
from yadisk import functions as yadisk_funcs

from app.app_config import *

from app.tools.yandex.exceptions import InvalidAuthTokenException

class DiskManager:

    def __init__(
            self,
            token: str, 
            local_template_dir: str = LOCAL_TEMPLATE_DIR,
            local_compiled_dir: str = LOCAL_COMPILED_DIR,
            remote_template_dir: str = REMOTE_TEMPLATE_DIR,
            remote_compiled_dir: str = REMOTE_COMPILED_DIR,
        ) -> None:
        self.session_generator : YaDisk = YaDisk(token=token)
        
        if not self.session_generator.check_token():
            raise InvalidAuthTokenException(
                "ERROR: Remote connection was not established: Invalid authentication token")

        self.local_template_dir = local_template_dir
        self.local_compiled_dir = local_compiled_dir
        self.remote_template_dir = remote_template_dir
        self.remote_compiled_dir = remote_compiled_dir


    def get_resource_meta(
            self,
            filename: str = "",
            remote_compiled_dir: str = REMOTE_COMPILED_DIR,
            ) -> Optional[Dict]:
        return yadisk_funcs.resources.get_meta(
            self.session_generator.get_session(),
            os.path.join(remote_compiled_dir, filename),
        )


    def upload(
            self,
            filename: str,
            overwrite: bool = False,
            local_compiled_dir: str = LOCAL_COMPILED_DIR,
            remote_compiled_dir: str = REMOTE_COMPILED_DIR,
        ) -> Tuple[bool, Optional[Dict]]:
        yadisk_funcs.upload(
            self.session_generator.get_session(),
            os.path.join(local_compiled_dir, filename),
            os.path.join(remote_compiled_dir, filename),
            overwrite=overwrite,
        )


    def download(
            self,
            filename: str,
            remote_template_dir: str = REMOTE_TEMPLATE_DIR,
            local_template_dir: str = LOCAL_TEMPLATE_DIR,
        ) -> None:
        yadisk_funcs.download(
            self.session_generator.get_session(),
            os.path.join(remote_template_dir, filename),
            os.path.join(local_template_dir, filename),
        )
        

    def publish(
            self,
            filename: str,
            remote_compiled_dir: str = REMOTE_COMPILED_DIR,
        ) -> None:
        yadisk_funcs.publish(
            self.session_generator.get_session(),
            os.path.join(remote_compiled_dir, filename),
        )