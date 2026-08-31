from typing import Literal

ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_delivery_controllers_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
