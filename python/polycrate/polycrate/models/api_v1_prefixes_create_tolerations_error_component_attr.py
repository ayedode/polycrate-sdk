from typing import Literal

ApiV1PrefixesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PREFIXES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_prefixes_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PrefixesCreateTolerationsErrorComponentAttr:
    if value in API_V1_PREFIXES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
