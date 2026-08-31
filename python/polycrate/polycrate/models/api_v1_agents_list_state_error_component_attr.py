from typing import Literal

ApiV1AgentsListStateErrorComponentAttr = Literal["state"]

API_V1_AGENTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AgentsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_agents_list_state_error_component_attr(value: str) -> ApiV1AgentsListStateErrorComponentAttr:
    if value in API_V1_AGENTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
