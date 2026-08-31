from typing import Literal

ApiV1PopsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_POPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pops_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
