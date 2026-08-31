from typing import Literal

ApiV1AlertsReconcileCreateCategoryErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTS_RECONCILE_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsReconcileCreateCategoryErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alerts_reconcile_create_category_error_component_code(
    value: str,
) -> ApiV1AlertsReconcileCreateCategoryErrorComponentCode:
    if value in API_V1_ALERTS_RECONCILE_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
