from typing import Literal

ApiV1PopsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_POPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsCreateAnnotationsErrorComponentAttr] = {
    "annotations",
}


def check_api_v1_pops_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PopsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_POPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
