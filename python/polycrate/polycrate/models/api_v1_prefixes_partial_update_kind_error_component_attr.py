from typing import Literal

ApiV1PrefixesPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PREFIXES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_prefixes_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdateKindErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
