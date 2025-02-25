from io import TextIOWrapper

class DeploymentDictionary:
    def __init__(self, deployment_dictionary_path: str) -> None:
        self.deployment_dictionary_path: str = deployment_dictionary_path
        self.deployment_dictionary_entries: dict[str, str] = {}
        self.new_deployment_dictionary_variables: dict[str, str] = {}

        self.load_deployment_dictionary_file()

    def load_deployment_dictionary_file(self) -> None:
        deployment_dictionary_entries = open(self.deployment_dictionary_path, 'r')

        self.save_all_deployment_dictionary_entries(deployment_dictionary_entries)

        deployment_dictionary_entries.close()

    def save_all_deployment_dictionary_entries(self, deployment_dictionary_entries : TextIOWrapper) -> None:
        for deployment_dictionary_entry in deployment_dictionary_entries:
            if len(deployment_dictionary_entry) > 0 and len(deployment_dictionary_entry.split('=')) == 2 :
                deployment_dictionary_entry = deployment_dictionary_entry.replace('\r', '').replace('\n', '')
                split_deployment_dictionary_entry = deployment_dictionary_entry.split('=')
                self.deployment_dictionary_entries.update(
                    { split_deployment_dictionary_entry[0] : split_deployment_dictionary_entry[1] }
                )

    def add_new_deployment_dictionary_variables(self, key: str, value: str) -> None:
        self.new_deployment_dictionary_variables.update({ key : value })

    def append_new_variables_to_deployment_dictionary_file(self) -> None:
        deployment_dictionary_entries = open(self.deployment_dictionary_path, 'a')

        self.save_all_new_deployment_dictionary_entries(deployment_dictionary_entries)

        deployment_dictionary_entries.close()

    def save_all_new_deployment_dictionary_entries(self, deployment_dictionary_entries : TextIOWrapper) -> None:
        for key, value in self.new_deployment_dictionary_variables.items():
            if not self.deployment_dictionary_entries.get(key):
                deployment_dictionary_entries.write(key + '=' + value)
