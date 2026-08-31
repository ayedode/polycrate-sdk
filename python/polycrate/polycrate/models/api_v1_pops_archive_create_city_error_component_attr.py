from typing import Literal

ApiV1PopsArchiveCreateCityErrorComponentAttr = Literal["city"]

API_V1_POPS_ARCHIVE_CREATE_CITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsArchiveCreateCityErrorComponentAttr] = {
    "city",
}


def check_api_v1_pops_archive_create_city_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreateCityErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_CITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_CITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
