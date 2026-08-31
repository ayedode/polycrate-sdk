from typing import Literal

ApiV1AlertroutersPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_alertrouters_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
