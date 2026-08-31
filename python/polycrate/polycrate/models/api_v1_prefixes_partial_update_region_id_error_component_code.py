from typing import Literal

ApiV1PrefixesPartialUpdateRegionIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PREFIXES_PARTIAL_UPDATE_REGION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdateRegionIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_prefixes_partial_update_region_id_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdateRegionIdErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_REGION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_REGION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
