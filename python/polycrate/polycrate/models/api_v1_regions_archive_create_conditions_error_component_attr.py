from typing import Literal

ApiV1RegionsArchiveCreateConditionsErrorComponentAttr = Literal["conditions"]

API_V1_REGIONS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateConditionsErrorComponentAttr
] = {
    "conditions",
}


def check_api_v1_regions_archive_create_conditions_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateConditionsErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
