from typing import Literal

ApiV1AlertroutersArchiveCreateLabelPodErrorComponentAttr = Literal["label_pod"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateLabelPodErrorComponentAttr
] = {
    "label_pod",
}


def check_api_v1_alertrouters_archive_create_label_pod_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateLabelPodErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
