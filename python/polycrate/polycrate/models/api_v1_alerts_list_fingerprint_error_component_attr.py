from typing import Literal

ApiV1AlertsListFingerprintErrorComponentAttr = Literal["fingerprint"]

API_V1_ALERTS_LIST_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListFingerprintErrorComponentAttr] = {
    "fingerprint",
}


def check_api_v1_alerts_list_fingerprint_error_component_attr(
    value: str,
) -> ApiV1AlertsListFingerprintErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
