import os

class EnvironmentContext:
    DEPLOYMENT_DICTIONARY_ENVIRONMENT_VARIABLE: str = 'DICO'
    CONFIG_FILES_DIRECTORY_ENVIRONMENT_VARIABLE: str = 'CONF'
    CONFIG_FILES_EXTENSION_ENVIRONMENT_VARIABLE: str = 'CONFIG_FILE_EXTENSION'

    def __init__(self) -> None:
        self.deployment_dictionary_path: str = os.environ.get(self.DEPLOYMENT_DICTIONARY_ENVIRONMENT_VARIABLE, '')
        self.config_files_directory: str = os.environ.get(self.CONFIG_FILES_DIRECTORY_ENVIRONMENT_VARIABLE, '')
        self.config_files_extension: str = os.environ.get(self.CONFIG_FILES_EXTENSION_ENVIRONMENT_VARIABLE, '')

        if (not self.is_environment_parameterized()):
            raise Exception('There are missing environment variables')

    def is_environment_parameterized(self) -> bool:
        return self.deployment_dictionary_path != '' and self.config_files_directory != '' and self.config_files_extension != ''
