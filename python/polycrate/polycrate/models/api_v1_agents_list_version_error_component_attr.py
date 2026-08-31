from typing import Literal

ApiV1AgentsListVersionErrorComponentAttr = Literal["version"]

API_V1_AGENTS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AgentsListVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_agents_list_version_error_component_attr(value: str) -> ApiV1AgentsListVersionErrorComponentAttr:
    if value in API_V1_AGENTS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
