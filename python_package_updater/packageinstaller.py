import platform
import socket
import os
import logging
from datetime import datetime

def setup_logging(log_directory):
    log_time = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
    log_path = os.path.join(log_directory, f"{log_time}.log")

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_package_manager():
    system_info = platform.freedesktop_os_release()
    if "Debian" in system_info['NAME'] or "Ubuntu" in system_info['NAME']:
        return "apt"
    elif "Fedora" in system_info['NAME'] or "Red Hat" in system_info['NAME'] or "CentOS" in system_info['NAME']:
        return "yum"
    else:
        return None

def update_system(package_manager):
    if package_manager == "apt":
        os.system("apt update && apt upgrade -y")
    elif package_manager == "yum":
        os.system("yum update -y")
    else:
        logging.error("Unsupported package manager")
        raise ValueError("Unsupported package manager")

def system_update_check():
    hostname = socket.gethostname()
    log_directory = "/var/log/pythensecupdater"
    setup_logging(log_directory)

    logging.info(f"Starting security check and update for {hostname}")

    package_manager = get_package_manager()
    if package_manager:
        logging.info(f"Detected package manager: {package_manager}")
        try:
            update_system(package_manager)
            logging.info("System update completed successfully")
        except Exception as e:
            logging.error(f"An error occurred during the update: {str(e)}")
    else:
        logging.error("Could not determine the package manager. Update aborted.")

    logging.info(f"Completed security check and update for {hostname}")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root.")
    else:
        system_update_check()
