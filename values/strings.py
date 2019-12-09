import os
from dotenv import load_dotenv
load_dotenv()


class Urls:
    editor_url = f"https://editor-url.{os.getenv('SANDBOX')}.voxmedia.com"


class LoginCredentials:
    editorUsername = os.getenv('EDITOR_USERNAME')
    editorPassword = os.getenv('EDITOR_PW')


class Cookies:
    editor_test_blog_password_cookie = {
        'name': "hub_abc_private_mode",
        'value': "abcdefghijklmnopqrstuvwxyz123456",
        'domain': "editor-blog.testeditor.com"
    }


class EntryTypeClasses:
    standard = "entry_template_standard"
