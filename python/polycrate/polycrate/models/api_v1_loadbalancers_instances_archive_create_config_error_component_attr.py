from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponentAttr = Literal["config"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_loadbalancers_instances_archive_create_config_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
