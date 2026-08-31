from typing import Literal

ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponentAttr = Literal["label_criticality"]

API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponentAttr
] = {
    "label_criticality",
}


def check_api_v1_alertrouters_ingest_create_label_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
