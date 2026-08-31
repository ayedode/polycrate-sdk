from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_regions_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
