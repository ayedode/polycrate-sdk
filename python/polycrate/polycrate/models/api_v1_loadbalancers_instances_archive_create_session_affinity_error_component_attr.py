from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponentAttr = Literal["session_affinity"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SESSION_AFFINITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponentAttr
] = {
    "session_affinity",
}


def check_api_v1_loadbalancers_instances_archive_create_session_affinity_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SESSION_AFFINITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SESSION_AFFINITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
