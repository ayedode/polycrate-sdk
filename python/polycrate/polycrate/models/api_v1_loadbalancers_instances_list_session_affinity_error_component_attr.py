from typing import Literal

ApiV1LoadbalancersInstancesListSessionAffinityErrorComponentAttr = Literal["session_affinity"]

API_V1_LOADBALANCERS_INSTANCES_LIST_SESSION_AFFINITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListSessionAffinityErrorComponentAttr
] = {
    "session_affinity",
}


def check_api_v1_loadbalancers_instances_list_session_affinity_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListSessionAffinityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_SESSION_AFFINITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_SESSION_AFFINITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
