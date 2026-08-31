from typing import Literal

ApiV1LoadbalancersRegionsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_regions_update_labels_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateLabelsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
