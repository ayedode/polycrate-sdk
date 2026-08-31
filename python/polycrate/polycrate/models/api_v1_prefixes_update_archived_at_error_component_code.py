from typing import Literal

ApiV1PrefixesUpdateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_PREFIXES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesUpdateArchivedAtErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_prefixes_update_archived_at_error_component_code(
    value: str,
) -> ApiV1PrefixesUpdateArchivedAtErrorComponentCode:
    if value in API_V1_PREFIXES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
