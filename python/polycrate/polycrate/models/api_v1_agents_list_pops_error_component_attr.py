from typing import Literal

ApiV1AgentsListPopsErrorComponentAttr = Literal["pops"]

API_V1_AGENTS_LIST_POPS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AgentsListPopsErrorComponentAttr] = {
    "pops",
}


def check_api_v1_agents_list_pops_error_component_attr(value: str) -> ApiV1AgentsListPopsErrorComponentAttr:
    if value in API_V1_AGENTS_LIST_POPS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_POPS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
