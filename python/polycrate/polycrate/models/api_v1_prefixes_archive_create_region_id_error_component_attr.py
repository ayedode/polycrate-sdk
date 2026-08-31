from typing import Literal

ApiV1PrefixesArchiveCreateRegionIdErrorComponentAttr = Literal["region_id"]

API_V1_PREFIXES_ARCHIVE_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateRegionIdErrorComponentAttr
] = {
    "region_id",
}


def check_api_v1_prefixes_archive_create_region_id_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateRegionIdErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
