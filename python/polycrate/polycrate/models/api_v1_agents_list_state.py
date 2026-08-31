from typing import Literal

ApiV1AgentsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_AGENTS_LIST_STATE_VALUES: set[ApiV1AgentsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_agents_list_state(value: str) -> ApiV1AgentsListState:
    if value in API_V1_AGENTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_STATE_VALUES!r}")
