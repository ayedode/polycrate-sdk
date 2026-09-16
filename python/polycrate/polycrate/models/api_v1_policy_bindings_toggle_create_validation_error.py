from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_policy_bindings_toggle_create_applied_error_component import (
        ApiV1PolicyBindingsToggleCreateAppliedErrorComponent,
    )
    from ..models.api_v1_policy_bindings_toggle_create_enabled_error_component import (
        ApiV1PolicyBindingsToggleCreateEnabledErrorComponent,
    )
    from ..models.api_v1_policy_bindings_toggle_create_execution_log_error_component import (
        ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponent,
    )
    from ..models.api_v1_policy_bindings_toggle_create_non_field_errors_error_component import (
        ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_policy_bindings_toggle_create_policy_id_error_component import (
        ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent,
    )
    from ..models.api_v1_policy_bindings_toggle_create_scope_error_component import (
        ApiV1PolicyBindingsToggleCreateScopeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PolicyBindingsToggleCreateValidationError")


@_attrs_define
class ApiV1PolicyBindingsToggleCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PolicyBindingsToggleCreateAppliedErrorComponent |
            ApiV1PolicyBindingsToggleCreateEnabledErrorComponent | ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponent
            | ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent |
            ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent | ApiV1PolicyBindingsToggleCreateScopeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PolicyBindingsToggleCreateAppliedErrorComponent
        | ApiV1PolicyBindingsToggleCreateEnabledErrorComponent
        | ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponent
        | ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent
        | ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent
        | ApiV1PolicyBindingsToggleCreateScopeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_policy_bindings_toggle_create_applied_error_component import (
            ApiV1PolicyBindingsToggleCreateAppliedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_enabled_error_component import (
            ApiV1PolicyBindingsToggleCreateEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_non_field_errors_error_component import (
            ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_policy_id_error_component import (
            ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_scope_error_component import (
            ApiV1PolicyBindingsToggleCreateScopeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsToggleCreateEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsToggleCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PolicyBindingsToggleCreateAppliedErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_policy_bindings_toggle_create_applied_error_component import (
            ApiV1PolicyBindingsToggleCreateAppliedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_enabled_error_component import (
            ApiV1PolicyBindingsToggleCreateEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_execution_log_error_component import (
            ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_non_field_errors_error_component import (
            ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_policy_id_error_component import (
            ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policy_bindings_toggle_create_scope_error_component import (
            ApiV1PolicyBindingsToggleCreateScopeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PolicyBindingsToggleCreateAppliedErrorComponent
                | ApiV1PolicyBindingsToggleCreateEnabledErrorComponent
                | ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponent
                | ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent
                | ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent
                | ApiV1PolicyBindingsToggleCreateScopeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_toggle_create_error_type_0 = (
                        ApiV1PolicyBindingsToggleCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_toggle_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_toggle_create_error_type_1 = (
                        ApiV1PolicyBindingsToggleCreatePolicyIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_toggle_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_toggle_create_error_type_2 = (
                        ApiV1PolicyBindingsToggleCreateEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_toggle_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_toggle_create_error_type_3 = (
                        ApiV1PolicyBindingsToggleCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_toggle_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policy_bindings_toggle_create_error_type_4 = (
                        ApiV1PolicyBindingsToggleCreateAppliedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policy_bindings_toggle_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_policy_bindings_toggle_create_error_type_5 = (
                    ApiV1PolicyBindingsToggleCreateExecutionLogErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_policy_bindings_toggle_create_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_policy_bindings_toggle_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_policy_bindings_toggle_create_validation_error.additional_properties = d
        return api_v1_policy_bindings_toggle_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
