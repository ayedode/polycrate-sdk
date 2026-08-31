from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_loadbalancers_regions_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
