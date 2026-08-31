from typing import Literal

ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_LOADBALANCERS_REGIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_loadbalancers_regions_create_annotations_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
