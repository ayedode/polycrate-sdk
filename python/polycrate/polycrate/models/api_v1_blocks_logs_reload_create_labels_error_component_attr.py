from typing import Literal

ApiV1BlocksLogsReloadCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_blocks_logs_reload_create_labels_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateLabelsErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
