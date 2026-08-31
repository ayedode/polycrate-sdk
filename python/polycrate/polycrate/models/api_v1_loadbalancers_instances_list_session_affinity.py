from typing import Literal

ApiV1LoadbalancersInstancesListSessionAffinity = Literal["cookie", "ip", "none"]

API_V1_LOADBALANCERS_INSTANCES_LIST_SESSION_AFFINITY_VALUES: set[ApiV1LoadbalancersInstancesListSessionAffinity] = {
    "cookie",
    "ip",
    "none",
}


def check_api_v1_loadbalancers_instances_list_session_affinity(
    value: str,
) -> ApiV1LoadbalancersInstancesListSessionAffinity:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_SESSION_AFFINITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_SESSION_AFFINITY_VALUES!r}"
    )
