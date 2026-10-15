from typing import Literal

CodeRepositoryScope = Literal["system", "user"]

CODE_REPOSITORY_SCOPE_VALUES: set[CodeRepositoryScope] = {
    "system",
    "user",
}


def check_code_repository_scope(value: str) -> CodeRepositoryScope:
    if value in CODE_REPOSITORY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_SCOPE_VALUES!r}")
