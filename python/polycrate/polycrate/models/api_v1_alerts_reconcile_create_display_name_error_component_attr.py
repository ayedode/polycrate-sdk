from typing import Literal

ApiV1AlertsReconcileCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_ALERTS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_alerts_reconcile_create_display_name_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateDisplayNameErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
