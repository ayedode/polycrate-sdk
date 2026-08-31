from typing import Literal

ApiV1AgentsListKindErrorComponentAttr = Literal["kind"]

API_V1_AGENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AgentsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_agents_list_kind_error_component_attr(value: str) -> ApiV1AgentsListKindErrorComponentAttr:
    if value in API_V1_AGENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
