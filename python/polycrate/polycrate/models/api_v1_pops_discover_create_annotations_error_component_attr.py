from typing import Literal

ApiV1PopsDiscoverCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_POPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pops_discover_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateAnnotationsErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
