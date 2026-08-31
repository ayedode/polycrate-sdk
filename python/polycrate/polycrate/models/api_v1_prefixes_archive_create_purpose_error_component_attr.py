from typing import Literal

ApiV1PrefixesArchiveCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_PREFIXES_ARCHIVE_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_prefixes_archive_create_purpose_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreatePurposeErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
