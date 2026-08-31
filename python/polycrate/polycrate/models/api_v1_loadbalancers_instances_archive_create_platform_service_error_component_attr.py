from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_loadbalancers_instances_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
