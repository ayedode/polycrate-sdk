from typing import Literal

ApiV1RegionsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_REGIONS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_regions_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
