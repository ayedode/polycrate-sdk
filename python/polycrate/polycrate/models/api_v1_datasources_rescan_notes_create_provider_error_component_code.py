from typing import Literal

ApiV1DatasourcesRescanNotesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_datasources_rescan_notes_create_provider_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateProviderErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
