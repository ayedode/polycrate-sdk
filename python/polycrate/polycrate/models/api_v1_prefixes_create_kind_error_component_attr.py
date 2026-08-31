from typing import Literal

ApiV1PrefixesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PREFIXES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_prefixes_create_kind_error_component_attr(value: str) -> ApiV1PrefixesCreateKindErrorComponentAttr:
    if value in API_V1_PREFIXES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
