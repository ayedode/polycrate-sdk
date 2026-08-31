from typing import Literal

ApiV1PrefixesArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PREFIXES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_prefixes_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
