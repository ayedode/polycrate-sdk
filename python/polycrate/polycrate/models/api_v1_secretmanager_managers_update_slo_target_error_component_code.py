from typing import Literal

ApiV1SecretmanagerManagersUpdateSloTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersUpdateSloTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_secretmanager_managers_update_slo_target_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateSloTargetErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
