from typing import Literal

CodeRepositoryRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[CodeRepositoryRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_code_repository_request_criticality_type_3_type_1(value: str) -> CodeRepositoryRequestCriticalityType3Type1:
    if value in CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
