from typing import Literal

ApiV1AlertroutersIngestCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTROUTERS_INGEST_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_alertrouters_ingest_create_labels_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
