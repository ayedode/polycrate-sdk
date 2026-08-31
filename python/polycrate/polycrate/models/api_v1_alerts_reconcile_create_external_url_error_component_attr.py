from typing import Literal

ApiV1AlertsReconcileCreateExternalUrlErrorComponentAttr = Literal["external_url"]

API_V1_ALERTS_RECONCILE_CREATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateExternalUrlErrorComponentAttr
] = {
    "external_url",
}


def check_api_v1_alerts_reconcile_create_external_url_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateExternalUrlErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
