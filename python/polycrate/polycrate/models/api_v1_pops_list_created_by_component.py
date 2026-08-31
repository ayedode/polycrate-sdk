from typing import Literal

ApiV1PopsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_POPS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1PopsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pops_list_created_by_component(value: str) -> ApiV1PopsListCreatedByComponent:
    if value in API_V1_POPS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_CREATED_BY_COMPONENT_VALUES!r}")
