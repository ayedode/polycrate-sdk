from typing import Literal

ApiV1PrefixesCreateRegionIdErrorComponentAttr = Literal["region_id"]

API_V1_PREFIXES_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesCreateRegionIdErrorComponentAttr] = {
    "region_id",
}


def check_api_v1_prefixes_create_region_id_error_component_attr(
    value: str,
) -> ApiV1PrefixesCreateRegionIdErrorComponentAttr:
    if value in API_V1_PREFIXES_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
