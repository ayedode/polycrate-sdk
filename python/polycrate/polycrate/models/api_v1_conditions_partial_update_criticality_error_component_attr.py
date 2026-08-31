from typing import Literal

ApiV1ConditionsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CONDITIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_conditions_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
