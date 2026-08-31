from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponentAttr = Literal["enable_websockets"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_WEBSOCKETS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponentAttr
] = {
    "enable_websockets",
}


def check_api_v1_loadbalancers_instances_archive_create_enable_websockets_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_WEBSOCKETS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_WEBSOCKETS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
