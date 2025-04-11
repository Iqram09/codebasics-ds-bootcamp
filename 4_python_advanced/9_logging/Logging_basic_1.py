import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
) # here level are diffrent like info , warning , debug etc :) , filename="log.txt" its the file where we can store information

logging.info("this is info message")  # this is like print("this is info message") but to display it use logging.basicConfig
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")
logging.debug("this is debug message")