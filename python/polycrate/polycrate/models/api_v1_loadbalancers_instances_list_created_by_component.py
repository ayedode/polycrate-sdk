from typing import Literal

ApiV1LoadbalancersInstancesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1LoadbalancersInstancesListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_loadbalancers_instances_list_created_by_component(
    value: str,
) -> ApiV1LoadbalancersInstancesListCreatedByComponent:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
