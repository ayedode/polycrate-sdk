from typing import Literal

ApiV1BlocksCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCKS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_blocks_create_labels_error_component_attr(value: str) -> ApiV1BlocksCreateLabelsErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
