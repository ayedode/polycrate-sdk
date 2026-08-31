from typing import Literal

ApiV1AlertroutersArchiveCreateLabelClusterErrorComponentAttr = Literal["label_cluster"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateLabelClusterErrorComponentAttr
] = {
    "label_cluster",
}


def check_api_v1_alertrouters_archive_create_label_cluster_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateLabelClusterErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
