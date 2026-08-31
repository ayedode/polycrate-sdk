from typing import Literal

ApiV1AlertroutersIngestCreateLabelClusterErrorComponentAttr = Literal["label_cluster"]

API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelClusterErrorComponentAttr
] = {
    "label_cluster",
}


def check_api_v1_alertrouters_ingest_create_label_cluster_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelClusterErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
