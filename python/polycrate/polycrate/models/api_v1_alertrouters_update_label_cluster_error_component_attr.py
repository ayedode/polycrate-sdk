from typing import Literal

ApiV1AlertroutersUpdateLabelClusterErrorComponentAttr = Literal["label_cluster"]

API_V1_ALERTROUTERS_UPDATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateLabelClusterErrorComponentAttr
] = {
    "label_cluster",
}


def check_api_v1_alertrouters_update_label_cluster_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateLabelClusterErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABEL_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
