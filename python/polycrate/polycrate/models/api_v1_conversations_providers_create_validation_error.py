from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conversations_providers_create_config_error_component import (
        ApiV1ConversationsProvidersCreateConfigErrorComponent,
    )
    from ..models.api_v1_conversations_providers_create_credential_error_component import (
        ApiV1ConversationsProvidersCreateCredentialErrorComponent,
    )
    from ..models.api_v1_conversations_providers_create_kind_error_component import (
        ApiV1ConversationsProvidersCreateKindErrorComponent,
    )
    from ..models.api_v1_conversations_providers_create_meta_error_component import (
        ApiV1ConversationsProvidersCreateMetaErrorComponent,
    )
    from ..models.api_v1_conversations_providers_create_name_error_component import (
        ApiV1ConversationsProvidersCreateNameErrorComponent,
    )
    from ..models.api_v1_conversations_providers_create_non_field_errors_error_component import (
        ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_conversations_providers_create_organization_error_component import (
        ApiV1ConversationsProvidersCreateOrganizationErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConversationsProvidersCreateValidationError")


@_attrs_define
class ApiV1ConversationsProvidersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConversationsProvidersCreateConfigErrorComponent |
            ApiV1ConversationsProvidersCreateCredentialErrorComponent | ApiV1ConversationsProvidersCreateKindErrorComponent
            | ApiV1ConversationsProvidersCreateMetaErrorComponent | ApiV1ConversationsProvidersCreateNameErrorComponent |
            ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent |
            ApiV1ConversationsProvidersCreateOrganizationErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConversationsProvidersCreateConfigErrorComponent
        | ApiV1ConversationsProvidersCreateCredentialErrorComponent
        | ApiV1ConversationsProvidersCreateKindErrorComponent
        | ApiV1ConversationsProvidersCreateMetaErrorComponent
        | ApiV1ConversationsProvidersCreateNameErrorComponent
        | ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent
        | ApiV1ConversationsProvidersCreateOrganizationErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conversations_providers_create_credential_error_component import (
            ApiV1ConversationsProvidersCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_kind_error_component import (
            ApiV1ConversationsProvidersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_meta_error_component import (
            ApiV1ConversationsProvidersCreateMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_name_error_component import (
            ApiV1ConversationsProvidersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_non_field_errors_error_component import (
            ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_organization_error_component import (
            ApiV1ConversationsProvidersCreateOrganizationErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsProvidersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsProvidersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsProvidersCreateOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsProvidersCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsProvidersCreateMetaErrorComponent):
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
        from ..models.api_v1_conversations_providers_create_config_error_component import (
            ApiV1ConversationsProvidersCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_credential_error_component import (
            ApiV1ConversationsProvidersCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_kind_error_component import (
            ApiV1ConversationsProvidersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_meta_error_component import (
            ApiV1ConversationsProvidersCreateMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_name_error_component import (
            ApiV1ConversationsProvidersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_non_field_errors_error_component import (
            ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_providers_create_organization_error_component import (
            ApiV1ConversationsProvidersCreateOrganizationErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConversationsProvidersCreateConfigErrorComponent
                | ApiV1ConversationsProvidersCreateCredentialErrorComponent
                | ApiV1ConversationsProvidersCreateKindErrorComponent
                | ApiV1ConversationsProvidersCreateMetaErrorComponent
                | ApiV1ConversationsProvidersCreateNameErrorComponent
                | ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent
                | ApiV1ConversationsProvidersCreateOrganizationErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_providers_create_error_type_0 = (
                        ApiV1ConversationsProvidersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_providers_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_providers_create_error_type_1 = (
                        ApiV1ConversationsProvidersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_providers_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_providers_create_error_type_2 = (
                        ApiV1ConversationsProvidersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_providers_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_providers_create_error_type_3 = (
                        ApiV1ConversationsProvidersCreateOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_providers_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_providers_create_error_type_4 = (
                        ApiV1ConversationsProvidersCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_providers_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_providers_create_error_type_5 = (
                        ApiV1ConversationsProvidersCreateMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_providers_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_providers_create_error_type_6 = (
                    ApiV1ConversationsProvidersCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_providers_create_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conversations_providers_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conversations_providers_create_validation_error.additional_properties = d
        return api_v1_conversations_providers_create_validation_error

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
