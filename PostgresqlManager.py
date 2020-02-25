from configparser import ConfigParser
import psycopg2


def get_connection_by_config(self, config_file_path, section_name):
    print('running')
    if len(config_file_path) > 0 and len(section_name) > 0:
        # Create an instance of ConfigParser class.
        config_parser = ConfigParser()
        # read the configuration file.
        config_parser.read(config_file_path)
        # if the configuration file contains the provided section name.
        if config_parser.has_section(section_name):
            print('1')
            # read the options of the section. the config_params is a list object.
            config_params = config_parser.items(section_name)
            # so we need below code to convert the list object to a python dictionary object.
            # define an empty dictionary.
            db_conn_dict = {}
            # loop in the list.
            for config_param in config_params:
                # get options key and value.
                key = config_param[0]
                value = config_param[1]
                # add the key value pair in the dictionary object.
                db_conn_dict[key] = value
            # get connection object use above dictionary object.
            conn = psycopg2.connect(**db_conn_dict)
            self._conn = conn
            print("******* get postgresql database connection with configuration file ********", "\n")
