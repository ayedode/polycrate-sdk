from typing import Literal

ApiV1LoadbalancersRegionsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1LoadbalancersRegionsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_loadbalancers_regions_list_created_by_component(
    value: str,
) -> ApiV1LoadbalancersRegionsListCreatedByComponent:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
