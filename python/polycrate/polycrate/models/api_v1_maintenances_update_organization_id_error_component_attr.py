from typing import Literal

ApiV1MaintenancesUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_MAINTENANCES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_maintenances_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
