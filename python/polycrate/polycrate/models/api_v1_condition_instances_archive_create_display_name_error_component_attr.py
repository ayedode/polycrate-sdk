from typing import Literal

ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_condition_instances_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
