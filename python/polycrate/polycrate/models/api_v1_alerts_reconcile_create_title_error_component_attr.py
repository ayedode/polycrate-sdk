from typing import Literal

ApiV1AlertsReconcileCreateTitleErrorComponentAttr = Literal["title"]

API_V1_ALERTS_RECONCILE_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateTitleErrorComponentAttr
] = {
    "title",
}


def check_api_v1_alerts_reconcile_create_title_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateTitleErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
