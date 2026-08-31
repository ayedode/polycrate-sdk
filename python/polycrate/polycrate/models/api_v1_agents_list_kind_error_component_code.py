from typing import Literal

ApiV1AgentsListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_AGENTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AgentsListKindErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_agents_list_kind_error_component_code(value: str) -> ApiV1AgentsListKindErrorComponentCode:
    if value in API_V1_AGENTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
