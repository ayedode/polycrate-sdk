from typing import Literal

ApiV1PrefixesPartialUpdatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_PREFIXES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_prefixes_partial_update_purpose_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdatePurposeErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
