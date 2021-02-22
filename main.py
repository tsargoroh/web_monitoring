#Coding Task for F-Secure

#ConfigParser is a Python class which implements a basic configuration language for Python programs
#The configuration files consist of sections followed by key/value pairs of options
from configparser import ConfigParser
import sys, re, time
import logging
import web, email_sender

def main():
    logging.basicConfig(level=logging.INFO, filename="web_info.log", format="%(levelname)s | %(asctime)s | %(message)s",
                        datefmt="%H:%M:%S %d.%m.%Y")
    CheckingPeriod = -1
    Email_Address = ""
    Email_Password = ""
    Receiver = ""
    required_config_files = ["settings.ini", "web_pages.ini"]
    config_parser = ConfigParser()
    #Set is a collection which is unordered and unindexed, no duplicate members are allowed
    #Set subtraction or .difference() can be used to see difference in collections
    #Alternative option using list comprehension:
    #missing_config_files = [x for x in required_config_files if x not in config_parser.read(required_config_files)]
    missing_config_files = set(required_config_files) - set(config_parser.read(required_config_files))
    if (len(missing_config_files) != 0):
        print("Missing configuration files:")
        for missing_config_file in missing_config_files:
            print(missing_config_file)
        sys.exit(0)
    if (config_parser.has_section("settings")):
        CheckingPeriod = int(config_parser.get("settings", "CheckingPeriod"))
        Email_Address = config_parser.get("settings", "Email_Address")
        Email_Password = config_parser.get("settings", "Email_Password")
        Receiver = config_parser.get("settings", "Receiver")
    if (CheckingPeriod == -1):
        print("Unable to read checking period from configuration files")
        sys.exit(0)
    while (True):
        failed_web_list = []
        for section in config_parser.sections():
            requirements_list = []
            url = None
            if (section != "settings"):
                for key, value in config_parser.items(section):
                    if (key == "url"):
                        url = config_parser.get(section, "url")
                    #using regex to check if the key is "reqx" where x is any positive integer or zero
                    elif (re.search("^req[0-9]+$", key) != None):
                        requirements_list.append(value)
                failed, status_code, error_type, response_time = web.request(url, requirements_list)
                if (failed == True):
                    failed_web_list.append([url, status_code, error_type, response_time])
        if (len(Email_Address) > 0 and len(Email_Password) > 0 and len(Receiver) > 0 and len(failed_web_list) > 0):
            email_sender.send_email(Email_Address, Email_Password, Receiver, failed_web_list)
        time.sleep(CheckingPeriod)

if __name__ == "__main__":
    main()