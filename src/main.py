from deployment_dictionary import DeploymentDictionary
from environment_context import EnvironmentContext
from configuration_deployment_utils import ConfigurationDeploymentUtils

def main() -> None:
    environment_context = EnvironmentContext()

    deployment_dictionary = DeploymentDictionary(environment_context.deployment_dictionary_path)

    configuration_deployment_utils = ConfigurationDeploymentUtils(
        environment_context.config_files_directory,
        environment_context.config_files_extension,
        deployment_dictionary.deployment_dictionary_entries)
    configuration_deployment_utils.replace_variables_in_all_config_files()

    deployment_dictionary.append_new_variables_to_deployment_dictionary_file()

if __name__ == '__main__':
    main()
