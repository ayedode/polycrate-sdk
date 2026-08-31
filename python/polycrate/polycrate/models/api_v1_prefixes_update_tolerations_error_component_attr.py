from typing import Literal

ApiV1PrefixesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PREFIXES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_prefixes_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PrefixesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PREFIXES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
