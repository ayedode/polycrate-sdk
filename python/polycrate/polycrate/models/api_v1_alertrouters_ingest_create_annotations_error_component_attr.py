from typing import Literal

ApiV1AlertroutersIngestCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ALERTROUTERS_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_alertrouters_ingest_create_annotations_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
