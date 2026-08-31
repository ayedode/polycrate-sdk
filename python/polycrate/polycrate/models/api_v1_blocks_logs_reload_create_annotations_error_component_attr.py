from typing import Literal

ApiV1BlocksLogsReloadCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_blocks_logs_reload_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
