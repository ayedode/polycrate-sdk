from typing import Literal

ApiV1PrefixesPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PREFIXES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_prefixes_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
