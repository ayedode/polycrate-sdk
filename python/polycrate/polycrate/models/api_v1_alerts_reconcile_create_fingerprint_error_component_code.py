from typing import Literal

ApiV1AlertsReconcileCreateFingerprintErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTS_RECONCILE_CREATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsReconcileCreateFingerprintErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alerts_reconcile_create_fingerprint_error_component_code(
    value: str,
) -> ApiV1AlertsReconcileCreateFingerprintErrorComponentCode:
    if value in API_V1_ALERTS_RECONCILE_CREATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
