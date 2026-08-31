from typing import Literal

ApiV1AlertroutersIngestCreateLabelPodErrorComponentAttr = Literal["label_pod"]

API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelPodErrorComponentAttr
] = {
    "label_pod",
}


def check_api_v1_alertrouters_ingest_create_label_pod_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelPodErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
