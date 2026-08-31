from typing import Literal

ApiV1ConditionsArchiveCreateIsSystemErrorComponentAttr = Literal["is_system"]

API_V1_CONDITIONS_ARCHIVE_CREATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateIsSystemErrorComponentAttr
] = {
    "is_system",
}


def check_api_v1_conditions_archive_create_is_system_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateIsSystemErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
