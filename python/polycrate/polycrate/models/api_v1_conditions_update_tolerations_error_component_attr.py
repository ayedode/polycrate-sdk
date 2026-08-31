from typing import Literal

ApiV1ConditionsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CONDITIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_conditions_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
