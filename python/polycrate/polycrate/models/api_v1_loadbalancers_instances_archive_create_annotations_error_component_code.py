from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_instances_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
