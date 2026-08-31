from typing import Literal

ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_rescan_notes_create_platform_service_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
