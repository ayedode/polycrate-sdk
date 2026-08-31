from typing import Literal

ApiV1ApmApmstacksListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_APM_APMSTACKS_LIST_STATE_NOT_VALUES: set[ApiV1ApmApmstacksListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_apm_apmstacks_list_state_not(value: str) -> ApiV1ApmApmstacksListStateNot:
    if value in API_V1_APM_APMSTACKS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_STATE_NOT_VALUES!r}")
