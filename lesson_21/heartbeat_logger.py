import json
import logging
from datetime import datetime
from logging import config
import pathlib


def setup_logging():
    config_file = pathlib.Path("./logger_config.json")
    with open(config_file) as file:
        desired_configuration = json.load(file)
    logging.config.dictConfig(desired_configuration)


logger = logging.getLogger(__name__)


class HeartbeatMonitoringLogger:
    __thread_pattern: str = "Key TSTFEED0300|7E3E|0400"
    __filtered_lines_list: list[str]

    def __init__(self, thread_pattern: str):
        setup_logging()
        self.__thread_pattern = thread_pattern

    def check_sys_return_logs(self):
        self.__filtered_lines_list = list(self.__lines_with_desired_pattern().__reversed__())

        for period, line in enumerate(self.__filtered_lines_list):
            if period < len(self.__filtered_lines_list) - 1:
                start_time: datetime = self.__time_into_datetime(
                    self.__timestamp_value_from_line(line))

                end_time: datetime = self.__time_into_datetime(
                    self.__timestamp_value_from_line(self.__filtered_lines_list[period + 1]))

                self.__log_from_time_restrictions(start_time, end_time)

    def __log_from_time_restrictions(self, start_time: datetime, end_time: datetime):
        error_time = end_time.strftime("%H:%M:%S")
        if 31 < (end_time - start_time).total_seconds() < 33:
            self.__warning_logs(error_time)
        elif (end_time - start_time).total_seconds() >= 33:
            self.__error_logs(error_time)

    def __time_into_datetime(self, str_time: str) -> datetime:
        return datetime.strptime(str_time, "%H:%M:%S")

    def __lines_with_desired_pattern(self) -> list[str]:
        with open("./hblog.txt", "r+") as file:
            return [line.strip() for line in file if line.find(self.__thread_pattern) != -1]

    def __timestamp_value_from_line(self, line: str) -> str:
        list_of_line_items: list[str] = line.split()
        return list_of_line_items[list_of_line_items.index("Timestamp") + 1]

    def __warning_logs(self, error_time: str) -> None:
        logger.warning(f"WARNING: Heartbeat between 31s and 33s at {error_time}")

    def __error_logs(self, error_time: str) -> None:
        logger.error(f"ERROR: Heartbeat is 33s or more at {error_time}")


# print(HeartbeatMonitoringLogger.get_lines_with_desired_pattern(HeartbeatMonitoringLogger))
heart_beat_monitoring_logger: HeartbeatMonitoringLogger = HeartbeatMonitoringLogger("Key TSTFEED0300|7E3E|0400")
# print(heart_beat_monitoring_logger.get_lines_with_desired_pattern())
heart_beat_monitoring_logger.check_sys_return_logs()
