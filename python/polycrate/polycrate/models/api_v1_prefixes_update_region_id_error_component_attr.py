from typing import Literal

ApiV1PrefixesUpdateRegionIdErrorComponentAttr = Literal["region_id"]

API_V1_PREFIXES_UPDATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesUpdateRegionIdErrorComponentAttr] = {
    "region_id",
}


def check_api_v1_prefixes_update_region_id_error_component_attr(
    value: str,
) -> ApiV1PrefixesUpdateRegionIdErrorComponentAttr:
    if value in API_V1_PREFIXES_UPDATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
