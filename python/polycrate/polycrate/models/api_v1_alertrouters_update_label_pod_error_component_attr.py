from typing import Literal

ApiV1AlertroutersUpdateLabelPodErrorComponentAttr = Literal["label_pod"]

API_V1_ALERTROUTERS_UPDATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateLabelPodErrorComponentAttr
] = {
    "label_pod",
}


def check_api_v1_alertrouters_update_label_pod_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateLabelPodErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
