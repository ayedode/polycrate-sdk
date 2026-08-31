from typing import Literal

ApiV1PrefixesArchiveCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_PREFIXES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_prefixes_archive_create_description_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateDescriptionErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
