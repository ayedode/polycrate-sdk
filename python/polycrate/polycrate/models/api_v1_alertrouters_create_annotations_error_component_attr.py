from typing import Literal

ApiV1AlertroutersCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ALERTROUTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_alertrouters_create_annotations_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
