from typing import Literal

ApiV1AlertsDiscoverCreateFingerprintErrorComponentAttr = Literal["fingerprint"]

API_V1_ALERTS_DISCOVER_CREATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateFingerprintErrorComponentAttr
] = {
    "fingerprint",
}


def check_api_v1_alerts_discover_create_fingerprint_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateFingerprintErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
