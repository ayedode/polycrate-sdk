from typing import Literal

ApiV1PrefixesCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_PREFIXES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesCreateArchivedAtErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_prefixes_create_archived_at_error_component_code(
    value: str,
) -> ApiV1PrefixesCreateArchivedAtErrorComponentCode:
    if value in API_V1_PREFIXES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
