from typing import Literal

ApiV1DatasourcesRescanNotesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_datasources_rescan_notes_create_kind_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateKindErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
