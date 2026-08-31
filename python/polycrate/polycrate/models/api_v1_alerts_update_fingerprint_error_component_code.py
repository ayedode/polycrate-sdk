from typing import Literal

ApiV1AlertsUpdateFingerprintErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_UPDATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateFingerprintErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_update_fingerprint_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateFingerprintErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
