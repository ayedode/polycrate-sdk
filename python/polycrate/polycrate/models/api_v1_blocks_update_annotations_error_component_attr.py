from typing import Literal

ApiV1BlocksUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCKS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateAnnotationsErrorComponentAttr] = {
    "annotations",
}


def check_api_v1_blocks_update_annotations_error_component_attr(
    value: str,
) -> ApiV1BlocksUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
