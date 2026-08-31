from typing import Literal

ApiV1AlertroutersCreateLabelPodErrorComponentAttr = Literal["label_pod"]

API_V1_ALERTROUTERS_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateLabelPodErrorComponentAttr
] = {
    "label_pod",
}


def check_api_v1_alertrouters_create_label_pod_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateLabelPodErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
