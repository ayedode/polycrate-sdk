from typing import Literal

ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_regions_update_annotations_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
