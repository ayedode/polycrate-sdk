from typing import Literal

ApiV1ConditionsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conditions_update_tolerations_error_component_code(
    value: str,
) -> ApiV1ConditionsUpdateTolerationsErrorComponentCode:
    if value in API_V1_CONDITIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
