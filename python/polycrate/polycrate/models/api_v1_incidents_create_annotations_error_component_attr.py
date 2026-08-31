from typing import Literal

ApiV1IncidentsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_INCIDENTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_incidents_create_annotations_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
