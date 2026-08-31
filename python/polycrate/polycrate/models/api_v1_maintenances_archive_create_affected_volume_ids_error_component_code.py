from typing import Literal

ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_MAINTENANCES_ARCHIVE_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_maintenances_archive_create_affected_volume_ids_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
