from typing import Literal

ApiV1LoadbalancersInstancesListScope = Literal["system", "user"]

API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_VALUES: set[ApiV1LoadbalancersInstancesListScope] = {
    "system",
    "user",
}


def check_api_v1_loadbalancers_instances_list_scope(value: str) -> ApiV1LoadbalancersInstancesListScope:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_VALUES!r}")
