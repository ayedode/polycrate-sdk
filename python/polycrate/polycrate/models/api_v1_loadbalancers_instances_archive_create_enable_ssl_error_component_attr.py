from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponentAttr = Literal["enable_ssl"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_SSL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponentAttr
] = {
    "enable_ssl",
}


def check_api_v1_loadbalancers_instances_archive_create_enable_ssl_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_SSL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_SSL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
