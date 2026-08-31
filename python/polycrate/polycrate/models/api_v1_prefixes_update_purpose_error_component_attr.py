from typing import Literal

ApiV1PrefixesUpdatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_PREFIXES_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesUpdatePurposeErrorComponentAttr] = {
    "purpose",
}


def check_api_v1_prefixes_update_purpose_error_component_attr(
    value: str,
) -> ApiV1PrefixesUpdatePurposeErrorComponentAttr:
    if value in API_V1_PREFIXES_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
