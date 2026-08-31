from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_loadbalancers_instances_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
