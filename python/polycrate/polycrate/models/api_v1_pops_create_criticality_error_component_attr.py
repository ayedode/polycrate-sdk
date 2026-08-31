from typing import Literal

ApiV1PopsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_POPS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsCreateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_pops_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PopsCreateCriticalityErrorComponentAttr:
    if value in API_V1_POPS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
