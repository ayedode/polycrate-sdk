from typing import Literal

ApiV1IncidentsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_INCIDENTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_incidents_update_labels_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateLabelsErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
