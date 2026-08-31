from typing import Literal

ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_loadbalancers_regions_update_annotations_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
