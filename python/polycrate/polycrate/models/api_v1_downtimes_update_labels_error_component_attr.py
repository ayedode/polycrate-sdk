from typing import Literal

ApiV1DowntimesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOWNTIMES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_downtimes_update_labels_error_component_attr(
    value: str,
) -> ApiV1DowntimesUpdateLabelsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
