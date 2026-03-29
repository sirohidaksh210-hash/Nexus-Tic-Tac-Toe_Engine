import logging
import datetime

class NexusLog:
    """Records session data for performance analysis."""
    def __init__(self):
        log_name = f"nexus_session_{datetime.date.today()}.log"
        logging.basicConfig(filename=log_name, level=logging.INFO)
        self.session_start = datetime.datetime.now()

    def record_action(self, actor, location):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {actor} occupied {location}"
        logging.info(entry)
        print(f"System: {entry}")

    def finalize(self, result):
        logging.info(f"Session Terminated. Result: {result}")
