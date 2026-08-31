from typing import Literal

ApiV1LoadbalancersRegionsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_LOADBALANCERS_REGIONS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_loadbalancers_regions_create_labels_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateLabelsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
