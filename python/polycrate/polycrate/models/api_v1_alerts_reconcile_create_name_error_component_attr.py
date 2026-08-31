from typing import Literal

ApiV1AlertsReconcileCreateNameErrorComponentAttr = Literal["name"]

API_V1_ALERTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_alerts_reconcile_create_name_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateNameErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
