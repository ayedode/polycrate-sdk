from typing import Literal

ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_INCIDENTS_ARCHIVE_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_incidents_archive_create_affected_host_ids_error_component_code(
    value: str,
) -> ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponentCode:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
