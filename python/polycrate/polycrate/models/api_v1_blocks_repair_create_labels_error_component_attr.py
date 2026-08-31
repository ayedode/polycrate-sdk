from typing import Literal

ApiV1BlocksRepairCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCKS_REPAIR_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksRepairCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_blocks_repair_create_labels_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateLabelsErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
