from typing import Literal

ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_rescan_notes_create_tolerations_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
