from typing import Literal

ApiV1AlertsUpdateFingerprintErrorComponentAttr = Literal["fingerprint"]

API_V1_ALERTS_UPDATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateFingerprintErrorComponentAttr] = {
    "fingerprint",
}


def check_api_v1_alerts_update_fingerprint_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateFingerprintErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
