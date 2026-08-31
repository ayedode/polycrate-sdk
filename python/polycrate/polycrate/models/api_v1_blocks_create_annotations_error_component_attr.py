from typing import Literal

ApiV1BlocksCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCKS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateAnnotationsErrorComponentAttr] = {
    "annotations",
}


def check_api_v1_blocks_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
