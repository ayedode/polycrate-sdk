from typing import Literal

ApiV1PrefixesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PREFIXES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_prefixes_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
