from typing import Literal

ApiV1AlertsReconcileCreateFingerprintErrorComponentAttr = Literal["fingerprint"]

API_V1_ALERTS_RECONCILE_CREATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateFingerprintErrorComponentAttr
] = {
    "fingerprint",
}


def check_api_v1_alerts_reconcile_create_fingerprint_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateFingerprintErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_FINGERPRINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
