from typing import Literal

ApiV1ConditionsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_CONDITIONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_conditions_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
