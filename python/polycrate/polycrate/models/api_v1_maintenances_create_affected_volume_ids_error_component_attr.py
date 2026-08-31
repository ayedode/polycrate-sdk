from typing import Literal

ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponentAttr = Literal["affected_volume_ids"]

API_V1_MAINTENANCES_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponentAttr
] = {
    "affected_volume_ids",
}


def check_api_v1_maintenances_create_affected_volume_ids_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
