from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PORTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_archive_create_ports_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PORTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PORTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
