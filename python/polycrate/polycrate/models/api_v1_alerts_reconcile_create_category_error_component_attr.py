from typing import Literal

ApiV1AlertsReconcileCreateCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTS_RECONCILE_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateCategoryErrorComponentAttr
] = {
    "category",
}


def check_api_v1_alerts_reconcile_create_category_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateCategoryErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
