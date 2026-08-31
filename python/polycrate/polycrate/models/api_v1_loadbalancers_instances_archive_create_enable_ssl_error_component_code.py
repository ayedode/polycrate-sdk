from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_SSL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_archive_create_enable_ssl_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_SSL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_SSL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
