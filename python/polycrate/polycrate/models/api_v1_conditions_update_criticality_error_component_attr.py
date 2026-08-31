from typing import Literal

ApiV1ConditionsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CONDITIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_conditions_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
