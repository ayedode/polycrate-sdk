from typing import Literal

ApiV1EndpointsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_ENDPOINTS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1EndpointsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_endpoints_list_created_by_component(value: str) -> ApiV1EndpointsListCreatedByComponent:
    if value in API_V1_ENDPOINTS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
