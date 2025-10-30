from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv
from . import settings
import os

def secret_key() -> str:
    """
    Retrieves or generates a secret key for the application.

    This function looks for the `SECRET_KEY` environment variable used for
    cryptography and security (e.g., in Django applications). The behavior follows this logic:

    1. **Initial Lookup:** Attempts to retrieve the value of `SECRET_KEY` 
       directly from the environment variables.
    2. **.env File Loading:** If the variable is not found in the environment, 
       the `.env` file (located in the project's base directory) is loaded.
    3. **Key Generation:** 
       - If the key still does not exist, the function generates a new random key 
         using `get_random_secret_key()`.
       - This new key is written into the `.env` file in the format 
         `SECRET_KEY=<generated_key>`.
       - The `.env` file is reloaded, and the new key is returned.
    4. **Return:** Always returns a valid `string` containing the secret key.

    Args:
        None

    Returns:
        str: The secret key retrieved or generated.
    """
    ENV_PATH = settings.BASE_DIR / '.env'
    key = os.getenv("SECRET_KEY")
    if key:
        return key
    else:
        load_dotenv(ENV_PATH)
        key = os.getenv('SECRET_KEY')
        if not key:
            with open(ENV_PATH, 'w') as f:
                f.write(f'SECRET_KEY={get_random_secret_key()}\n')
            load_dotenv(ENV_PATH)
            key = os.getenv('SECRET_KEY')
            return key
        else:
            return key