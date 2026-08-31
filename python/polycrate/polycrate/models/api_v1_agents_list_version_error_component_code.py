from typing import Literal

ApiV1AgentsListVersionErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_AGENTS_LIST_VERSION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AgentsListVersionErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_agents_list_version_error_component_code(value: str) -> ApiV1AgentsListVersionErrorComponentCode:
    if value in API_V1_AGENTS_LIST_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
