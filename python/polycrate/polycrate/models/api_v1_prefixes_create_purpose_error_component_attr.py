from typing import Literal

ApiV1PrefixesCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_PREFIXES_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesCreatePurposeErrorComponentAttr] = {
    "purpose",
}


def check_api_v1_prefixes_create_purpose_error_component_attr(
    value: str,
) -> ApiV1PrefixesCreatePurposeErrorComponentAttr:
    if value in API_V1_PREFIXES_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
