from typing import Literal

ApiV1AlertsReconcileCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_alerts_reconcile_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
