"""
All constants will be declared here
"""

# Standard constants
GLOBAL_CONFIG_INFO = "configInfo"
GLOBAL_STREAM_INFO = "streamsInfo"
GLOBAL_STREAM_ID_LIST = "streamsIdList"
GLOBAL_STREAM_TC_NAME_LIST = "streamsTcNameList"
HTTP_PROTOCOL = "http://"
HTTPS_PROTOCOL = "https://"
HEADERS = {"content-type": "application/json", "accept": "application/json", "Source-Type": "SMS", "Source-Id": "123"}
BLANK = ""
INVALID = "INVALID"
STREAM_NAME = "StreamName"
VLE_REQUEST_PARAMS = "VLE_REQUEST_PARAMS"
VALIDATOR_TYPE = "VALIDATOR_TYPE"
MPD_FILE_EXTENSION = ".m3u8"


# Component end-points
class EndPoint(object):
    A8_RECORD = "/a8/record"
    N8_CONFIGURATION = "/configuration"
    N8_ADD_STREAMS = "/addstreams"


# Test framework related constants
class TestDirectory(object):
    CONFIG_DIR = "conf"
    TEST_DIR = "tests"
    OUTPUT_DIR = "output"
    TOOLS_DIR = "tools"

# Recording statuses
class RecordingStatus(object):
    STARTED = "STARTED"
    STARTED_WITH_ERROR = "STARTEDWITHERROR"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    INCOMPLETE = "INCOMPLETE"
    PENDING = "PENDING"
