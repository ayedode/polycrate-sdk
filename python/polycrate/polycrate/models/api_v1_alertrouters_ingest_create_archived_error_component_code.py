from typing import Literal

ApiV1AlertroutersIngestCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_INGEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_ingest_create_archived_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreateArchivedErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
