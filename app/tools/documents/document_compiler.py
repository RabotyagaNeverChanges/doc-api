from typing import Dict

from docxtpl import DocxTemplate

from app.app_config import *

def delete_template_after_compilation(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("WARNING: File does not exists!")

def compile_template(
        filename: str,
        context: Dict,
        template_dir: str = LOCAL_TEMPLATE_DIR,
        compiled_dir: str = LOCAL_COMPILED_DIR,
    ) -> None:
        file_url = os.path.join(template_dir, filename)
        
        template = DocxTemplate(file_url)
        template.render(context)
        template.save(os.path.join(compiled_dir, filename))

        delete_template_after_compilation(file_url)

