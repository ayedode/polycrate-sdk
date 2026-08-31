from typing import Literal

ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponentAttr = Literal["affected_volume_ids"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponentAttr
] = {
    "affected_volume_ids",
}


def check_api_v1_maintenances_partial_update_affected_volume_ids_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
