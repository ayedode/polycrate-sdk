from typing import Literal

ApiV1AlertroutersUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTROUTERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertroutersUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_alertrouters_update_labels_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateLabelsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
