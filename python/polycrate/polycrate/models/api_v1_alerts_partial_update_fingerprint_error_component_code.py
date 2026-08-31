from typing import Literal

ApiV1AlertsPartialUpdateFingerprintErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_PARTIAL_UPDATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateFingerprintErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_partial_update_fingerprint_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateFingerprintErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
