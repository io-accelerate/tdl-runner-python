from tdl.runner.challenge_session_config import ChallengeSessionConfig
from tdl.queue.implementation_runner_config import ImplementationRunnerConfig
from credentials_config_file import read_from_config_file, read_from_config_file_with_default


class Utils:

    @staticmethod
    def get_config():
        return ChallengeSessionConfig\
            .for_journey(read_from_config_file('tdl_journey_id'))\
            .with_server_hostname(read_from_config_file('tdl_hostname'))\
            .with_colours(read_from_config_file_with_default('tdl_use_coloured_output', True))\
            .with_recording_system_should_be_on(read_from_config_file_with_default('tdl_require_rec', True))\
            .with_working_directory('../')

    @staticmethod
    def get_runner_config():
        return ImplementationRunnerConfig()\
            .set_unique_id(read_from_config_file('tdl_username'))\
            .set_hostname(read_from_config_file('tdl_hostname'))
