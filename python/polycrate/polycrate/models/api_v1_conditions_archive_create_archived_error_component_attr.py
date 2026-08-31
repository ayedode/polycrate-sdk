from typing import Literal

ApiV1ConditionsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CONDITIONS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_conditions_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
