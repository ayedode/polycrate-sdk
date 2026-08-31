from typing import Literal

ApiV1RegionsUpdateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_REGIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsUpdateArchivedAtErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_regions_update_archived_at_error_component_code(
    value: str,
) -> ApiV1RegionsUpdateArchivedAtErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
