from typing import Literal

ApiV1AlertroutersCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ALERTROUTERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_alertrouters_create_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateCriticalityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
