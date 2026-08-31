from typing import Literal

ApiV1DatasourcesIngestCreateNameErrorComponentAttr = Literal["name"]

API_V1_DATASOURCES_INGEST_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_datasources_ingest_create_name_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateNameErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
