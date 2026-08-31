from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponentAttr = Literal["ports"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PORTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponentAttr
] = {
    "ports",
}


def check_api_v1_loadbalancers_instances_archive_create_ports_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PORTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PORTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
