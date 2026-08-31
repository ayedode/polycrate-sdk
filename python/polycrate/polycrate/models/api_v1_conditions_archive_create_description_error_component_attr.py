from typing import Literal

ApiV1ConditionsArchiveCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_CONDITIONS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_conditions_archive_create_description_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateDescriptionErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
