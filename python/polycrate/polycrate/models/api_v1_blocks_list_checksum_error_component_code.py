from typing import Literal

ApiV1BlocksListChecksumErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_BLOCKS_LIST_CHECKSUM_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksListChecksumErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_blocks_list_checksum_error_component_code(value: str) -> ApiV1BlocksListChecksumErrorComponentCode:
    if value in API_V1_BLOCKS_LIST_CHECKSUM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_CHECKSUM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
