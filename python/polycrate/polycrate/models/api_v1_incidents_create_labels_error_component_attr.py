from typing import Literal

ApiV1IncidentsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_INCIDENTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_incidents_create_labels_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateLabelsErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
