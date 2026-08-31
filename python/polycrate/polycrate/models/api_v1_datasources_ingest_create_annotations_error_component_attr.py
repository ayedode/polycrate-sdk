from typing import Literal

ApiV1DatasourcesIngestCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DATASOURCES_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_datasources_ingest_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
