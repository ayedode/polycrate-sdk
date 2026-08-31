from typing import Literal

ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_maintenances_partial_update_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
