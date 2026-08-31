from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_credentials_update_api_endpoint_error_component import (
        ApiV1CredentialsUpdateApiEndpointErrorComponent,
    )
    from ..models.api_v1_credentials_update_api_key_error_component import ApiV1CredentialsUpdateApiKeyErrorComponent
    from ..models.api_v1_credentials_update_api_user_error_component import ApiV1CredentialsUpdateApiUserErrorComponent
    from ..models.api_v1_credentials_update_kubeconfig_error_component import (
        ApiV1CredentialsUpdateKubeconfigErrorComponent,
    )
    from ..models.api_v1_credentials_update_metadata_error_component import ApiV1CredentialsUpdateMetadataErrorComponent
    from ..models.api_v1_credentials_update_non_field_errors_error_component import (
        ApiV1CredentialsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_credentials_update_ssh_private_key_error_component import (
        ApiV1CredentialsUpdateSshPrivateKeyErrorComponent,
    )
    from ..models.api_v1_credentials_update_ssh_public_key_error_component import (
        ApiV1CredentialsUpdateSshPublicKeyErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CredentialsUpdateValidationError")


@_attrs_define
class ApiV1CredentialsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CredentialsUpdateApiEndpointErrorComponent | ApiV1CredentialsUpdateApiKeyErrorComponent |
            ApiV1CredentialsUpdateApiUserErrorComponent | ApiV1CredentialsUpdateKubeconfigErrorComponent |
            ApiV1CredentialsUpdateMetadataErrorComponent | ApiV1CredentialsUpdateNonFieldErrorsErrorComponent |
            ApiV1CredentialsUpdateSshPrivateKeyErrorComponent | ApiV1CredentialsUpdateSshPublicKeyErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CredentialsUpdateApiEndpointErrorComponent
        | ApiV1CredentialsUpdateApiKeyErrorComponent
        | ApiV1CredentialsUpdateApiUserErrorComponent
        | ApiV1CredentialsUpdateKubeconfigErrorComponent
        | ApiV1CredentialsUpdateMetadataErrorComponent
        | ApiV1CredentialsUpdateNonFieldErrorsErrorComponent
        | ApiV1CredentialsUpdateSshPrivateKeyErrorComponent
        | ApiV1CredentialsUpdateSshPublicKeyErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_credentials_update_api_endpoint_error_component import (
            ApiV1CredentialsUpdateApiEndpointErrorComponent,
        )
        from ..models.api_v1_credentials_update_api_key_error_component import (
            ApiV1CredentialsUpdateApiKeyErrorComponent,
        )
        from ..models.api_v1_credentials_update_api_user_error_component import (
            ApiV1CredentialsUpdateApiUserErrorComponent,
        )
        from ..models.api_v1_credentials_update_kubeconfig_error_component import (
            ApiV1CredentialsUpdateKubeconfigErrorComponent,
        )
        from ..models.api_v1_credentials_update_non_field_errors_error_component import (
            ApiV1CredentialsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_credentials_update_ssh_private_key_error_component import (
            ApiV1CredentialsUpdateSshPrivateKeyErrorComponent,
        )
        from ..models.api_v1_credentials_update_ssh_public_key_error_component import (
            ApiV1CredentialsUpdateSshPublicKeyErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CredentialsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsUpdateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsUpdateApiUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsUpdateApiKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsUpdateKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsUpdateSshPrivateKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsUpdateSshPublicKeyErrorComponent):
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
        from ..models.api_v1_credentials_update_api_endpoint_error_component import (
            ApiV1CredentialsUpdateApiEndpointErrorComponent,
        )
        from ..models.api_v1_credentials_update_api_key_error_component import (
            ApiV1CredentialsUpdateApiKeyErrorComponent,
        )
        from ..models.api_v1_credentials_update_api_user_error_component import (
            ApiV1CredentialsUpdateApiUserErrorComponent,
        )
        from ..models.api_v1_credentials_update_kubeconfig_error_component import (
            ApiV1CredentialsUpdateKubeconfigErrorComponent,
        )
        from ..models.api_v1_credentials_update_metadata_error_component import (
            ApiV1CredentialsUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_credentials_update_non_field_errors_error_component import (
            ApiV1CredentialsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_credentials_update_ssh_private_key_error_component import (
            ApiV1CredentialsUpdateSshPrivateKeyErrorComponent,
        )
        from ..models.api_v1_credentials_update_ssh_public_key_error_component import (
            ApiV1CredentialsUpdateSshPublicKeyErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CredentialsUpdateApiEndpointErrorComponent
                | ApiV1CredentialsUpdateApiKeyErrorComponent
                | ApiV1CredentialsUpdateApiUserErrorComponent
                | ApiV1CredentialsUpdateKubeconfigErrorComponent
                | ApiV1CredentialsUpdateMetadataErrorComponent
                | ApiV1CredentialsUpdateNonFieldErrorsErrorComponent
                | ApiV1CredentialsUpdateSshPrivateKeyErrorComponent
                | ApiV1CredentialsUpdateSshPublicKeyErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_update_error_type_0 = (
                        ApiV1CredentialsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_update_error_type_1 = (
                        ApiV1CredentialsUpdateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_update_error_type_2 = (
                        ApiV1CredentialsUpdateApiUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_update_error_type_3 = (
                        ApiV1CredentialsUpdateApiKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_update_error_type_4 = (
                        ApiV1CredentialsUpdateKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_update_error_type_5 = (
                        ApiV1CredentialsUpdateSshPrivateKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_update_error_type_6 = (
                        ApiV1CredentialsUpdateSshPublicKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_credentials_update_error_type_7 = (
                    ApiV1CredentialsUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_credentials_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_credentials_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_credentials_update_validation_error.additional_properties = d
        return api_v1_credentials_update_validation_error

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
