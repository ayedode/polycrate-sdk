from typing import Literal

ApiV1AlertsListFingerprintErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ALERTS_LIST_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsListFingerprintErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_alerts_list_fingerprint_error_component_code(
    value: str,
) -> ApiV1AlertsListFingerprintErrorComponentCode:
    if value in API_V1_ALERTS_LIST_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_FINGERPRINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
