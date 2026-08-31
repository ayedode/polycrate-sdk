from typing import Literal

ApiV1DatasourcesIngestCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DATASOURCES_INGEST_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_datasources_ingest_create_labels_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateLabelsErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
