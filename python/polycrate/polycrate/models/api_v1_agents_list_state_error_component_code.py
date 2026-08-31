from typing import Literal

ApiV1AgentsListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_AGENTS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AgentsListStateErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_agents_list_state_error_component_code(value: str) -> ApiV1AgentsListStateErrorComponentCode:
    if value in API_V1_AGENTS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
