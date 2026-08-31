from typing import Literal

ApiV1AgentsListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_AGENTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AgentsListNameExactErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_agents_list_name_exact_error_component_code(value: str) -> ApiV1AgentsListNameExactErrorComponentCode:
    if value in API_V1_AGENTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
