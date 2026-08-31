from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_loadbalancers_instances_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
