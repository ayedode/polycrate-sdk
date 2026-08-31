from typing import Literal

ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_datasources_rescan_notes_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
