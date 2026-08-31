from typing import Literal

ApiV1PrefixesPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_prefixes_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
