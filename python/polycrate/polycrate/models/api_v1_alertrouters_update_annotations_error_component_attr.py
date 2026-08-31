from typing import Literal

ApiV1AlertroutersUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ALERTROUTERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_alertrouters_update_annotations_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
