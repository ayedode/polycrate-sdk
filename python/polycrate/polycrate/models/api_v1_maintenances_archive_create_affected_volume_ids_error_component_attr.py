from typing import Literal

ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponentAttr = Literal["affected_volume_ids"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponentAttr
] = {
    "affected_volume_ids",
}


def check_api_v1_maintenances_archive_create_affected_volume_ids_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
