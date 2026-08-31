from typing import Literal

ApiV1PrefixesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PREFIXES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_prefixes_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
