from typing import Literal

ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_datasources_rescan_notes_create_provider_id_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
