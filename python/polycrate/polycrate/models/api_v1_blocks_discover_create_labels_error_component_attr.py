from typing import Literal

ApiV1BlocksDiscoverCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCKS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_blocks_discover_create_labels_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateLabelsErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
