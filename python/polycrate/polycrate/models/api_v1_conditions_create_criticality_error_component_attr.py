from typing import Literal

ApiV1ConditionsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CONDITIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_conditions_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ConditionsCreateCriticalityErrorComponentAttr:
    if value in API_V1_CONDITIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
