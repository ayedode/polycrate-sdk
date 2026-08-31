from typing import Literal

ApiV1BlocksRepairCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCKS_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_blocks_repair_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
