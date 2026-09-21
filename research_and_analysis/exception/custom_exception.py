import sys
import traceback
from typing import Optional, cast


class ResearchAnalystException(Exception):
    """Base exception class for research analyst errors"""
    def __init__(self, error_message, error_detail: Optional[object] = None):

        if isinstance(error_message, BaseException):
            norm_msg = str(error_message)
        else:
            norm_msg = str(error_message)

        exc_type = exc_value = exc_tb = None
        if error_detail is None:
            exc_type, exc_value, exc_tb = sys.exc_info()
        else:
            if hasattr(error_detail, "exc_info"):
                exc_info_obj = cast(sys, error_detail)
                exc_type, exc_value, exc_tb = exc_info_obj.exc_info()
            elif isinstance(error_detail, BaseException):
                exc_type, exc_value, exc_tb = type(error_detail), error_detail, error_detail.__traceback__
            else:
                exc_type, exc_value, exc_tb = sys.exc_info()

        last_tb = exc_tb
        while last_tb and last_tb.tb_next:
            last_tb = last_tb.tb_next

        self.filename = last_tb.tb_frame.f_code.co_filename if last_tb else "<unknown>"
        self.lineno = last_tb.tb_lineno if last_tb else -1
        self.error_message = norm_msg

        if exc_type and exc_tb:
            self.traceback_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            self.traceback_str = ""

        super().__init__(self.__str__())

    def __str__(self):
        base = f"Error in [{self.filename}] at line [{self.lineno}] | Message: {self.error_message}"
        if self.traceback_str:
            return f"{base}\nTraceback:\n{self.traceback_str}"
        return base

    def __repr__(self):
        return f"ResearchAnalystException(filename={self.filename!r}, lineno={self.lineno}, message={self.error_message!r})"
