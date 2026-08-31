from typing import Literal

ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponentAttr = Literal["datasource_url"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponentAttr
] = {
    "datasource_url",
}


def check_api_v1_datasources_rescan_notes_create_datasource_url_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
