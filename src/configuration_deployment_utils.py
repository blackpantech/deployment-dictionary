from glob import glob

class ConfigurationDeploymentUtils:
    def __init__(self, config_files_directory: str,
        config_files_extension: str,
        deployment_dictionary_entries: dict[str, str]) -> None:

        self.config_files_paths: list[str] = []
        self.config_files_directory: str = config_files_directory
        self.config_files_extension: str = config_files_extension
        self.deployment_dictionary_entries: dict[str, str] = deployment_dictionary_entries
        self.lookup_config_files()

    def lookup_config_files(self) -> None:
        self.config_files_paths = glob(self.config_files_directory + '*.' + self.config_files_extension)

    def replace_variables_in_all_config_files(self) -> None:
        for config_file_path in self.config_files_paths:
            self.replace_variables_in_config_file(config_file_path)

    def replace_variables_in_config_file(self, config_file_path: str) -> None:
        config_file_content, config_file_variables = self.read_config_file(config_file_path)

        config_file_content = self.replace_content(config_file_content, config_file_variables)

        self.write_config_file(config_file_path, config_file_content)

    def read_config_file(self, config_file_path: str) -> tuple[str, set[str]]:
        config_file_lines = open(config_file_path, 'r')
        config_file_content: str = ''
        config_file_variables: set[str] = set()

        for config_file_line in config_file_lines:
            start_index = config_file_line.find('{{')
            end_index = config_file_line.find('}}')

            if start_index < end_index and start_index > 0 and end_index > 0:
                # Removing whitespaces surrounding variables
                target_variable = config_file_line[start_index + 2 : end_index].strip()
                config_file_line = config_file_line.replace(
                    config_file_line[start_index : end_index + 2],
                    '{{' + target_variable + '}}'
                )
                config_file_variables.add(target_variable)

            config_file_content += config_file_line

        config_file_lines.close()

        return config_file_content, config_file_variables

    def replace_content(self, config_file_content: str, config_file_variables: set[str]) -> str:
        for config_file_variable in config_file_variables:
            if self.deployment_dictionary_entries.get(config_file_variable):
                config_file_content = config_file_content.replace(
                    '{{' + config_file_variable + '}}',
                    self.deployment_dictionary_entries.get(config_file_variable, '')
                )
            else:
                print('Missing variable in deployment dictionary: ' + config_file_variable)

        return config_file_content

    def write_config_file(self, config_file_path: str, config_file_content: str) -> None:
        config_file_writer = open(config_file_path, 'w')
        config_file_writer.write(config_file_content)
        config_file_writer.close()
