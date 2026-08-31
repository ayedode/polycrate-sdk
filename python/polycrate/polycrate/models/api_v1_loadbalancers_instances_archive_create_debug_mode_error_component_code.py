from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
