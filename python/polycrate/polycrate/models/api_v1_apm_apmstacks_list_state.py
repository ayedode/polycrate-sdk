from typing import Literal

ApiV1ApmApmstacksListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_APM_APMSTACKS_LIST_STATE_VALUES: set[ApiV1ApmApmstacksListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_apm_apmstacks_list_state(value: str) -> ApiV1ApmApmstacksListState:
    if value in API_V1_APM_APMSTACKS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_STATE_VALUES!r}")
