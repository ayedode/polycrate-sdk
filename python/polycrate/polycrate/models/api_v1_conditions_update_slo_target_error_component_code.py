from typing import Literal

ApiV1ConditionsUpdateSloTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_CONDITIONS_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsUpdateSloTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_conditions_update_slo_target_error_component_code(
    value: str,
) -> ApiV1ConditionsUpdateSloTargetErrorComponentCode:
    if value in API_V1_CONDITIONS_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
