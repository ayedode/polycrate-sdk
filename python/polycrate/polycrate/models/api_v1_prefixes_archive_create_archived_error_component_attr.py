from typing import Literal

ApiV1PrefixesArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PREFIXES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_prefixes_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
