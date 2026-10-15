from typing import Literal

CodeRepositoryRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CodeRepositoryRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_code_repository_request_criticality_type_2_type_1(value: str) -> CodeRepositoryRequestCriticalityType2Type1:
    if value in CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
